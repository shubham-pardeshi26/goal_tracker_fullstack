import uuid
from django.db import models
from datetime import datetime, timedelta
from django.db.models.signals import pre_save
from django.dispatch import receiver

# User_Model
class Users(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.IntegerField(max_length=10, unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

# Goal_Model
class Goal(models.Model):
    pass

# To-do List_Model
class TodoList(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Always set due_date to the next day at 12:00 AM
        self.due_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        super().save(*args, **kwargs)