from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=80)
    url = models.URLField()
    image = models.URLField()

    def __str__(self):
        return self.name