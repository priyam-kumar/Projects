from django.db import models

# Create your models here.
class studentsrecord(models.Model):
    registration_no = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    department = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    father_email = models.CharField(max_length=30)

    def __str__(self):
        return self.registration_no
