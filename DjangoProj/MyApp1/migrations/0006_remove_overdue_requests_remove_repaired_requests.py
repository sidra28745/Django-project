# Generated by Django 5.0.3 on 2024-03-29 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp1', '0005_overdue_requests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overdue',
            name='requests',
        ),
        migrations.RemoveField(
            model_name='repaired',
            name='requests',
        ),
    ]