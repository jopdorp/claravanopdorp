# Generated by Django 3.2.9 on 2022-04-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20220404_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='photo',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]