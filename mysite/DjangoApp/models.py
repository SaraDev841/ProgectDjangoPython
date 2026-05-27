from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    #TextField
    desc = models.TextField(max_length=1000)
    destDate = models.DateField()
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In_Progress', 'In Progress'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    performer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} , {self.status}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('Manager', 'מנהל'),
        ('Employee', 'עובד'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Employee')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.role}"

