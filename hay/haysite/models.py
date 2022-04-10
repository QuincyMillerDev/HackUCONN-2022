from pyexpat import model
from statistics import multimode
from django.db import models


class Person(models.Model):
    id_num = models.IntegerField(default=0, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.id_num
    
    @property
    def get_avg(self):
        data = self.data_set.all()
        avg = sum(data) / len(data)
        return avg


class Questions(models.Model):
    content = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.name)

class Data(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.IntegerField(default=0, blank=True, null=True)
    question = models.ForeignKey(Questions, on_delete=models.SET_NULL, blank=True, null=True)
    response = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}-{}".format(self.question, self.date)

