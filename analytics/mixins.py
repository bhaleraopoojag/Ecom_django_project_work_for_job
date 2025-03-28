from .signals import object_viewed_signal


class ObjectViewedMixin(object):
    def get_context_data(self,*args,**kwargs):
        context = super(ObjectViewedMixin ,self).get_context_data(*args,**kwargs) # type: ignore
        request = self.request # type: ignore
        instance =context.get('object')
        if instance:
            object_viewed_signal.send(instance.__class__,instance=instance,request=request)
        return context