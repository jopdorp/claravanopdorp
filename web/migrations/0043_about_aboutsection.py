# Generated by Django 3.2.9 on 2022-06-02 12:31

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0042_auto_20220602_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('intro', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=20)),
                ('contain', django_quill.fields.QuillField(blank=True, default=None)),
                ('details', models.TextField(blank=True)),
                ('video', models.FileField(default='', upload_to='')),
                ('url', models.CharField(default='', max_length=256)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.about')),
            ],
        ),
    ]
