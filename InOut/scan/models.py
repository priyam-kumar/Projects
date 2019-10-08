from django.db import models
from record.models import studentsrecord
# Create your models here.
class entryrecord(models.Model):
    registration_no = models.ForeignKey(studentsrecord,on_delete=models.CASCADE)
    purpose =   models.CharField(max_length=30)
    place   =   models.CharField(max_length=30)
    exit_time = models.DateTimeField(auto_now_add=True)
    entry_time  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.exit_time.strftime("%Y-%m-%d %H:%M:%S") + " -to- " + self.entry_time.strftime("%Y-%m-%d %H:%M:%S")
