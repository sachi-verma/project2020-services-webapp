from django.db import models

# Create your models here.
class User_message(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField()

class User_feedback(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Feedback = models.TextField()    


