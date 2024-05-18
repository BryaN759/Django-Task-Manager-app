from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title       = models.CharField(max_length=100, null=True)
    
    description = models.CharField(max_length=500, null=True, blank=True)

    data_posted = models.DateTimeField(auto_now_add=True)

    due_date    = models.DateField()

    images      = models.ImageField(upload_to='task_images/', null=True, blank=True)

    priority    =  models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='LOW')

    complete    = models.BooleanField(default=False, blank=True)

    user        = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.title



