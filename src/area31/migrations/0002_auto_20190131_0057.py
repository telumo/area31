# Generated by Django 2.1.5 on 2019-01-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area31', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='enter_year',
            field=models.IntegerField(blank=True, choices=[('1990', '1990'), ('1991', '1991'), ('1992', '1992')], null=True, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grad_year',
            field=models.IntegerField(blank=True, choices=[('1990', '1990'), ('1991', '1991'), ('1992', '1992')], null=True, verbose_name='year'),
        ),
    ]
