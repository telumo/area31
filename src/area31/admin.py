from django.contrib import admin
from .models import LocationLabel, Location
from .models import User, Profile
# from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(LocationLabel)
admin.site.register(Location)
# admin.site.register(Profile)