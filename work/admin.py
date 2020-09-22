from django.contrib import admin
from work.models import *
# Register your models here.
admin.site.register(Staff)
admin.site.register(Doctor)
admin.site.register(Appointments)
admin.site.register(Patient)
admin.site.register(MedicalRecords)
admin.site.register(LabTest)
