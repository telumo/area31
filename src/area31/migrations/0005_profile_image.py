# Generated by Django 2.1.5 on 2019-01-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area31', '0004_auto_20190131_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='プロフィール画像'),
        ),
    ]
