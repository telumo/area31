from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


GENDER_CHOICES = (
    ("女性", "女性"),
    ("男性", "男性"),
)
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(blank=True)
    
    def __str__(self):
       return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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