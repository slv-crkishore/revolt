from django.contrib import admin
from app.models import UserModel, Classes, School
# Register your models here.

admin.site.register(UserModel)
admin.site.register(Classes)
admin.site.register(School)
