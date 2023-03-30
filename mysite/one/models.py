from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
            ('doctor', 'Doctor'),
            ('patient', 'patient'),
            ('staff', 'staff')
        )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    # def __str__(self):
    #     return self.name

class DoctorDetail(models.Model):
    doctor_number = models.CharField(max_length = 30, unique=True)
    doctor_degree = models.CharField(max_length= 30)
    address = models.CharField(max_length= 100)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class PatentDetail(models.Model):
    patent_number = models.CharField(max_length= 15)
    patent_age = models.IntegerField()
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class StaffDetail(models.Model):
    staff_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Appointment(models.Model):
    patient_id = models.ForeignKey(PatentDetail, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(DoctorDetail, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    fees = models.IntegerField()