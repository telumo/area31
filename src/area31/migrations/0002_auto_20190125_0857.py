# Generated by Django 2.0.4 on 2019-01-24 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area31', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='user',
            field=models.ForeignKey(help_text='Specific Departments for this user.', on_delete=django.db.models.deletion.CASCADE, related_name='user_set', related_query_name='user', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
