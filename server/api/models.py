from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField

class Alarm(models.Model):
    title = models.CharField(max_length=100)
    time = models.TimeField(db_index = True, auto_now=False, auto_now_add=False)
    added_at = models.DateTimeField(default=timezone.now)
    color = ColorField(default='#52E8FF')

    def __str__(self):
        return self.title+" at "+str(self.time)