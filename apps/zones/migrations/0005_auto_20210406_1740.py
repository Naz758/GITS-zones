# Generated by Django 3.2 on 2021-04-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0004_auto_20210406_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='zone',
        ),
        migrations.AddField(
            model_name='agency',
            name='zone',
            field=models.ManyToManyField(to='zones.Zone'),
        ),
    ]