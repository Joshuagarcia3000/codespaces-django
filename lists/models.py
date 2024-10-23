from django.db import models
from django.contrib.auth.models import User
from voting.managers import VoteManager

class List(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = VoteManager()
    def __str__(self):
        return self.name
