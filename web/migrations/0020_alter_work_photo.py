# Generated by Django 3.2.9 on 2022-04-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_work_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
