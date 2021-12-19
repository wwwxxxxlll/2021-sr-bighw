from django.db import models
# Create your models here.

class Contributors(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=128,unique=False)
    repo_name = models.CharField(max_length=128,unique=False)
    con_name = models.CharField(max_length=128,unique=False)
    con_num = models.IntegerField()

class Commits(models.Model):
    id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=128)
    repo_name = models.CharField(max_length=128)
    con_name = models.CharField(max_length=128)

class date(models.Model):
    id = models.AutoField(primary_key=True)
    date_newest = models.DateTimeField()



