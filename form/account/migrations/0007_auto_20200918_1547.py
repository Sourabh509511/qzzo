# Generated by Django 3.1 on 2020-09-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200918_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Unique_id',
            field=models.CharField(default='MUFhpM', max_length=6),
        ),
    ]