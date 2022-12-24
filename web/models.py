from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
