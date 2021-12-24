from django.db import models

# Create your models here.
class people(models.Model):
     name=models.CharField(max_length=250)
     img=models.ImageField(upload_to = 'pics/')
     disc=models.TextField()
     
     def __str__(self):
          return self.name

class place(models.Model):
     name=models.CharField(max_length=250)
     img=models.ImageField(upload_to ='pics/')
     disc=models.TextField()

     def __str__(self):
          return self.name