# Generated by Django 3.2.9 on 2022-04-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_worksection_feet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worksection',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]