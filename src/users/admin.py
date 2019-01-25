from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

# # Register your models here.
# @admin.register(Department)
# class AdminDepartment(admin.ModelAdmin):
#     pass

@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email', 'gender', 'grad_year', 'entered_year')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'full_name', 'is_staff', 'gender', 'grad_year', 'entered_year')
    search_fields = ('username', 'full_name', 'email', 'gender', 'grad_year', 'entered_year')
    filter_horizontal = ('groups', 'user_permissions')

