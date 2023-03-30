from django.contrib import admin

# Register your models here.
from .models import Appointment,PatentDetail,DoctorDetail,CustomUser

admin.site.register(Appointment)
admin.site.register(PatentDetail)
admin.site.register(DoctorDetail)
admin.site.register(CustomUser)