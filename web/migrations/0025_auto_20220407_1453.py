# Generated by Django 3.2.9 on 2022-04-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_alter_worksection_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechnologyIcons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=20)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='worksection',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]