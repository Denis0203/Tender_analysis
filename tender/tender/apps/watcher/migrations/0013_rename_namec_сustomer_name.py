# Generated by Django 4.0.3 on 2022-06-10 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0012_rename_name_сustomer_namec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='сustomer',
            old_name='namec',
            new_name='name',
        ),
    ]
