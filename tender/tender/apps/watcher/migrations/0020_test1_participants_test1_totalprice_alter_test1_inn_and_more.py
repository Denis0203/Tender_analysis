# Generated by Django 4.0.3 on 2022-06-18 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watcher', '0019_alter_test1_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='test1',
            name='participants',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='test1',
            name='totalprice',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='test1',
            name='inn',
            field=models.ForeignKey(blank=True, db_column='watcher_inn', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='watcher.inn'),
        ),
        migrations.AlterModelTable(
            name='inn',
            table='watcher_inn',
        ),
    ]
