from django.contrib import admin
from .models import LocationLabel, Location
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

admin.site.register(LocationLabel)
admin.site.register(Location)