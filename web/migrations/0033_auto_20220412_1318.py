# Generated by Django 3.2.9 on 2022-04-12 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_alter_work_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='github_url',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='work',
            name='url',
            field=models.CharField(default='', max_length=256),
        ),
    ]