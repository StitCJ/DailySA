from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Solved(models.Model):
    problem_id = models.ForeignKey('main.Problem', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
