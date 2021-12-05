from django.db import models
#from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    events = models.ForeignKey("Event", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name
