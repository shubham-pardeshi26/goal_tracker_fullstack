# Generated by Django 5.0.1 on 2024-02-05 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_goal_users_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal_users',
            name='first_name',
            field=models.CharField(help_text='Enter your first name', max_length=30, verbose_name='First Name132546'),
        ),
        migrations.AlterField(
            model_name='goal_users',
            name='last_name',
            field=models.CharField(help_text='Enter your last name', max_length=30, verbose_name='Last Name1326541'),
        ),
    ]
