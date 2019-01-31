
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from area31.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.utils.functional import cached_property


@method_decorator(login_required, name='dispatch')
class MapView(TemplateView):
    template_name = "map.html"

    def get(self, request, *args, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class UserListView(TemplateView):
    template_name = "users.html"

    @cached_property
    def get_users(self):
        return User.objects.all()

    def get(self, request, *args, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
