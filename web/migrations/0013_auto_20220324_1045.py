# Generated by Django 3.2.9 on 2022-03-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='url',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='work',
            name='video',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
