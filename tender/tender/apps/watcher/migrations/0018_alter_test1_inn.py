# Generated by Django 4.0.3 on 2022-06-10 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0017_rename_idcust_inn_idi_inn_inn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test1',
            name='inn',
            field=models.ForeignKey(blank=True, db_column='watcher_inn', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='watcher.inn'),
        ),
    ]