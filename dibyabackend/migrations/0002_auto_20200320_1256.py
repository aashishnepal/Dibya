# Generated by Django 3.0.1 on 2020-03-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dibyabackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='due',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='paid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='rate',
            field=models.IntegerField(),
        ),
    ]