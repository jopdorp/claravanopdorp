# Generated by Django 3.2.9 on 2022-04-06 13:15

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_alter_work_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='photo',
        ),
        migrations.CreateModel(
            name='WorkSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=20)),
                ('reference', models.TextField(blank=True)),
                ('content', django_quill.fields.QuillField(blank=True, default=None)),
                ('photo', models.ImageField(default='', upload_to='')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.work')),
            ],
        ),
    ]