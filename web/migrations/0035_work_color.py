# Generated by Django 3.2.9 on 2022-05-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_worksection_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='color',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]