# Generated by Django 4.1.4 on 2023-02-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmodel',
            name='created_at',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='createmodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]