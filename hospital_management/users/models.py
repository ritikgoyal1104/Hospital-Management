from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Patient(models.Model):
    user=OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=50,null=True)
    dob=models.DateField(default=datetime.date.today())

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Doctor(models.Model):
    user=OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10)
    department=models.CharField(max_length=40,default="General")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


# class Disease(models.Model):
#     disease=models.CharField(max_length=50)
    
#     def __str__(self):
#         return f'{self.disease}'


class Slots(models.Model):
    slot1=models.TimeField(null=True)
    slot2=models.TimeField(null=True)
    slot3=models.TimeField(null=True)
    slot4=models.TimeField(null=True)
    slot5=models.TimeField(null=True)
    doctor=OneToOneField(Doctor,on_delete=models.CASCADE,related_name="slots")

    def __str__(self):
        return f'{self.doctor.user.first_name} {self.doctor.user.last_name}'

class Appointments(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="checkups")
    # disease=models.ManyToManyField(Disease)
    # prescription=models.TextField()
    slot=models.TimeField(null=True)

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.user.last_name} consulted {self.doctor.user.first_name} {self.doctor.user.last_name}'

class TempAppointments(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # disease=models.ManyToManyField(Disease)
    # prescription=models.TextField()
    slot=models.TimeField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.user.last_name} wants to consult {self.doctor.user.first_name} {self.doctor.user.last_name}'
