# Generated by Django 4.1.3 on 2022-12-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='sources',
            field=models.TextField(blank=True),
        ),
    ]
