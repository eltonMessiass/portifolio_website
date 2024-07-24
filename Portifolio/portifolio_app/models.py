from django.db import models

# Create your models here.

class Tools(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tools = models.ManyToManyField(Tools, null=True, blank=True)
    github = models.CharField(null=True, blank=True)
    view_live = models.CharField(null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name