# Generated by Django 2.1.3 on 2018-11-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181122_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='main.Status', verbose_name='Статус'),
        ),
    ]