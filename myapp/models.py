from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='assets/')
    title = models.CharField(max_length= 300, blank = True)
    gitrepo = models.TextField(blank=True)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.title