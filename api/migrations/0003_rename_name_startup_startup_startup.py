# Generated by Django 3.2.3 on 2021-05-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210522_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='name_startup',
            new_name='startup',
        ),
    ]
