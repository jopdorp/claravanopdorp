# Generated by Django 3.2.5 on 2021-07-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_page_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footersection',
            name='title',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
