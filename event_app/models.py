
# Create your models here.
from django.db import models

class Event(models.Model):
    date = models.DateField()
    heading = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    drive_link = models.URLField(blank=True)

    def __str__(self):
        return self.heading
