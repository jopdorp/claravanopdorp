# Generated by Django 3.2.9 on 2022-04-12 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_alter_worksection_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='technologyicons',
            old_name='content',
            new_name='icon_class',
        ),
    ]
