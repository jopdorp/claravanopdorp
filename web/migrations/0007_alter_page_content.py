# Generated by Django 3.2.5 on 2021-07-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_pagesection_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
