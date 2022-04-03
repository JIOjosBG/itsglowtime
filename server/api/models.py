from django.db import models
from django.utils import timezone

class Alarm(models.Model):
    title = models.CharField(max_length=100)
    time = models.TimeField(db_index = True, auto_now=False, auto_now_add=False)
    added_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title+" at "+str(self.time)