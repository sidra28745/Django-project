# Generated by Django 5.0.3 on 2024-03-29 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp1', '0008_delete_maintenance_alter_overdue_assetid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repaired',
            name='status',
            field=models.IntegerField(choices=[(0, 'not started'), (1, 'progress'), (2, 'completed')], default=0),
        ),
    ]