# Generated by Django 3.2.9 on 2022-03-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_pagesection_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('content', models.TextField(blank=True)),
                ('is_published', models.BooleanField()),
            ],
        ),
    ]