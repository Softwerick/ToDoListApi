from django.db import models


class tasks(models.Model):
    task = models.CharField(max_length=100, blank=True)
    done = models.BooleanField()

    def __str__(self):
        return self.task