# Generated by Django 3.2.5 on 2021-08-16 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20210816_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagesection',
            name='title',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
