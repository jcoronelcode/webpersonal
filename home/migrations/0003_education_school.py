# Generated by Django 5.1.6 on 2025-02-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_education_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.CharField(default='Default school', max_length=100, verbose_name='centro educativo'),
        ),
    ]
