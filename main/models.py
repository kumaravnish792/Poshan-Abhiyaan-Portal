from django.db import models
from patient.models import Patient
from django.db.models.signals import post_save
# Create your models here.
class Dose(models.Model):
    date_of_dose = models.DateField()
    status       = models.BooleanField(default=True)
    patient      = models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_of_dose)
