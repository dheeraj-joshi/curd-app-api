# Generated by Django 4.1.4 on 2023-02-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_alter_createmodel_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmodel',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]