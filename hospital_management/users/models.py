from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Patient(models.Model):
    user=OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Doctor(models.Model):
    user=OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=10)
    start_time=models.TimeField(auto_now=True)
    end_time=models.TimeField()
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Disease(models.Model):
    disease=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.disease}'


class Appointments(models.Model):
    patient=models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    doctor=models.ForeignKey(User, on_delete=models.CASCADE, related_name="checkups")
    disease=models.ManyToManyField(Disease)
    prescription=models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.user.last_name} consulted {self.doctor.user.first_name} {self.doctor.user.last_name}'
