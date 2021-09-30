# Generated by Django 3.2.7 on 2021-09-30 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210930_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrier',
            name='comments',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrier_comments', to='api.comment'),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='truckload_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='type', to='api.shipper'),
        ),
        migrations.AlterField(
            model_name='contactuser',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='contactuser_comments', to='api.comment'),
        ),
    ]
