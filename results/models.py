from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=1)
    standard=models.IntegerField()
    marks1=models.IntegerField()
    instrument = models.CharField(choices=(
            ('g', "Guitar"),
            ('b', "Bass"),
            ('d', "Drums"),
        ),
        max_length=1,null=True
    )
    marks2=models.IntegerField()
    marks3=models.IntegerField()
    marks4=models.IntegerField()
    sem=models.CharField(null=True, max_length=5)
    # image=models.ImageField(upload_to=filePath,null=True,blank=True)