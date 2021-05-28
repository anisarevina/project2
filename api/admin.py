from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
from .models import *

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Sector)
admin.site.register(LogoImage)
admin.site.register(StartUp)

