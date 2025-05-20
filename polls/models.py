from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Survey + Owner
class Survey(models.Model):

    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=50)
    purpose = models.TextField()

    def __str__(self):
        return str(self.title)

class Question(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)


class Choice(models.Model):
    qn = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    one = models.CharField(max_length=20, blank=True)
    two = models.CharField(max_length=20, blank=True)
    three = models.CharField(max_length=20, blank=True)
    four = models.CharField(max_length=20, blank=True)
    five = models.CharField(max_length=20, blank=True)

    def __str__(self):

        return str(self.qn)


