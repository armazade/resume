from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='experiences') # Many-to-many relationship with Skill

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    graduation_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)