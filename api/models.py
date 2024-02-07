import uuid
from django.db import models
from datetime import datetime, timedelta
from django.db.models.signals import pre_save
from django.dispatch import receiver


# User_Model
class Goal_Users(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(
        max_length=30,
        help_text="Enter your first name",
        verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=30, help_text="Enter your last name", verbose_name="Last Name"
    )
    mobile = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} | {self.email}"

    def save(self, *args, **kwargs):
        # Ensure the email is always saved in lowercase
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def create_user(self, validated_data):
        user = Goal_Users.objects.create_user(**validated_data)
        return user


# To-do List_Model
class TodoList(models.Model):
    user_id = models.ForeignKey(Goal_Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Always set due_date to the next day at 12:00 AM
        self.due_date = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        ) + timedelta(days=1)
        super().save(*args, **kwargs)


class Goal(models.Model):
    # Enum-like classes for goal_type and category
    class GoalType(models.TextChoices):
        SHORT = "short", "Short"
        MID = "mid", "Mid"
        LONG = "long", "Long"

    class Category(models.TextChoices):
        PERSONAL = "personal", "Personal"
        PROFESSIONAL = "professional", "Professional"
        OTHERS = "others", "Others"

    class Status_type(models.TextChoices):
        COMPLETED = "completed", "Completed"
        IN_PROGRESS = "in_progress", "In_progress"
        PAUSED = "paused", "Paused"

    user_id = models.ForeignKey(Goal_Users, on_delete=models.CASCADE)
    goal_type = models.CharField(
        max_length=10, choices=GoalType.choices, default=GoalType.SHORT
    )
    status = models.CharField(
        max_length=20, choices=Status_type.choices, default=Status_type.IN_PROGRESS
    )
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.PERSONAL
    )
    description = models.TextField()
    title = models.CharField(max_length=100)
    due_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user_id} | {self.title}"
