# Generated by Django 2.1.5 on 2019-02-01 08:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area31', '0011_auto_20190201_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Specific Departments for this user.', on_delete=django.db.models.deletion.CASCADE, related_name='user_set', related_query_name='user', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
