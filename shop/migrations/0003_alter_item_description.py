# Generated by Django 3.2.16 on 2022-11-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20221101_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
