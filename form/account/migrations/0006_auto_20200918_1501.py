# Generated by Django 3.1 on 2020-09-18 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200918_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Unique_id',
            field=models.CharField(default='0Le2DR', max_length=6),
        ),
    ]