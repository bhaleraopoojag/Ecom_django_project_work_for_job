
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .signals import object_viewed_signal
from .utils import get_client_ip
from django.contrib.sessions.models import Session
from django.db.models.signals import pre_save,post_save
from accounts.signals import user_logged_in


User=settings.AUTH_USER_MODEL

#  a setting that forces a user to only have one active session,
FORCE_SESSION_TO_ONE = getattr(settings,'FORCE_SESSION_TO_ONE',False)
FORCE_INACTIVE_USER_ENDSESSION = getattr(settings,'FORCE_INACTIVE_USER_ENDSESSION',False)


# Create your models here.
class ObjectViewedModel(models.Model):
    user          =  models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE) #user instance instance id
    ip_address    = models.CharField(max_length=220,blank=True,null=True)
    content_type  =  models.ForeignKey(ContentType,on_delete=models.CASCADE) #User,Product,Order,Cart,Address
    object_id     =  models.PositiveIntegerField() #Product id,Order id,
    content_object  =GenericForeignKey('content_type','object_id') #product instance
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed on %s" %(self.content_object,self.timestamp)
    
    class Meta:
        ordering = ['-timestamp']   #most recent saved show up first
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'

def object_viewed_receiver(sender,instance,request,*args,**kwargs):
    c_type= ContentType.objects.get_for_model(sender)
    new_view_obj = ObjectViewedModel.objects.create(
                    user=request.user,
                    content_type = c_type,
                    object_id = instance.id,
                    ip_address = get_client_ip(request)

    )

object_viewed_signal.connect(object_viewed_receiver)


class UserSession(models.Model):
    user          =  models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE) #user instance instance id
    ip_address    = models.CharField(max_length=220,blank=True,null=True)
    session_key   =models.CharField(max_length=100,blank=True,null=True)
    timestamp= models.DateTimeField(auto_now_add=True)
    active  = models.BooleanField(default=True)
    ended  = models.BooleanField(default=False)

    def end_session(self):
        session_key = self.session_key
        self.active = False
        self.ended = True
        self.save()
        try:
            Session.objects.get(pk=session_key).delete()
            ended =True
        except:
            pass 
        return self.ended
    



def post_save_session_receiver(sender,instance,created,*args,**kwargs):
    if created:
        qs = UserSession.objects.filter(user=instance.user,ended=False,active=False).exclude(id=instance.id)
        for i in qs:
            i.end_session()   
    if not instance.active and not instance.ended:
        instance.end_session()
if FORCE_SESSION_TO_ONE:
    post_save.connect(post_save_session_receiver,sender=UserSession)


def post_save_user_changed_receiver(sender,instance,created,*args,**kwargs):
    if not created:
        if instance.is_active ==False:
            qs = UserSession.objects.filter(user=instance.user,ended=False,active=False)
            for i in qs:
                i.end_session()

if FORCE_INACTIVE_USER_ENDSESSION:
    post_save.connect(post_save_user_changed_receiver,sender=User)



def user_logged_in_receiver(sender,instance,request,*args,**kwargs):
    user = instance
    ip_address = get_client_ip(request)
    session_key =request.session.session_key
    UserSession.objects.create(
            user=user,
            ip_address=ip_address,
            session_key=session_key
    )

user_logged_in.connect(user_logged_in_receiver)
    




