# Generated by Django 3.0.3 on 2020-04-06 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='expired',
            field=models.DateField(blank=True, null=True),
        ),
    ]
