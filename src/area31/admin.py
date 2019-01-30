from django.contrib import admin
from .models import LocationLabel, Location
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

admin.site.register(LocationLabel)
admin.site.register(Location)
admin.site.register(Profile)