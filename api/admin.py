# Register your models here.
from django.contrib import admin
from .models import Goal, TodoList, Goal_Users

admin.site.register(Goal)
admin.site.register(TodoList)
admin.site.register(Goal_Users)
