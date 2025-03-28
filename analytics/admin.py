from django.contrib import admin
from .models import ObjectViewedModel,UserSession

# Register your models here.
admin.site.register(ObjectViewedModel)
admin.site.register(UserSession)