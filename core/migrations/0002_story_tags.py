# Generated by Django 4.0.2 on 2025-04-20 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(related_name='stories', to='core.Tag'),
        ),
    ]
