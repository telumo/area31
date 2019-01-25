from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

# class User(models.Model):

#     # 名前
#     name = models.CharField(max_length=128)
#     # メールアドレス
#     email = models.EmailField()

class LocationLabel(models.Model):

    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label

class Location(models.Model):

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name=_('ユーザー'),
        blank=False,
        help_text=_('Specific Departments for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    latitude = models.CharField(
        max_length=10,
        blank=False,
    )

    longitude = models.CharField(
        max_length=10,
        blank=False,
    )

    label = models.ForeignKey(LocationLabel,
        on_delete=models.CASCADE,
        verbose_name=_('場所のラベル'),
        blank=False,
        # help_text=_('Specific Departments for this user.'),
        # related_name="user_set",
        # related_query_name="user",
    )

    def __str__(self):
        return self.latitude + ", " + self.longitude