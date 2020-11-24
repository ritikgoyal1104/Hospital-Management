from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointments)
admin.site.register(Departments)
admin.site.register(TempAppointments)