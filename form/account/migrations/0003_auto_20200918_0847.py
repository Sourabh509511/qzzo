# Generated by Django 3.1 on 2020-09-18 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200918_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Unique_id',
            field=models.CharField(blank=True, default='ebuwtd', max_length=6, null=True),
        ),
    ]
