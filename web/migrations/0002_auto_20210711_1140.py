# Generated by Django 3.2.5 on 2021-07-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='path',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]
