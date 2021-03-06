# Generated by Django 2.1.5 on 2019-01-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area31', '0003_auto_20190131_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='enter_year',
            field=models.IntegerField(blank=True, choices=[(1990, 1990), (1991, 1991), (1992, 1992)], null=True, verbose_name='卒業年'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grad_year',
            field=models.IntegerField(blank=True, choices=[(1990, 1990), (1991, 1991), (1992, 1992)], null=True, verbose_name='入学年'),
        ),
    ]
