from django.db import models

class Moviesapp(models.Model):
    cover=models.FileField(upload_to='Moviesapp/cover',null=True,blank=True)
    name=models.CharField(max_length=20)
    year=models.IntegerField()
    details=models.CharField(max_length=200)

    def __str__(self):
        return self.name