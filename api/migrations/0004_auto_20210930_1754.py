# Generated by Django 3.2.7 on 2021-09-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210930_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='location',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='career',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
