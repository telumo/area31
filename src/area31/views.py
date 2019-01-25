
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from area31.models import *


class MapView(TemplateView):
    template_name = "map.html"

    def get(self, request, *args, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class UserListView(TemplateView):
    template_name = "users.html"

    def get(self, request, *args, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class RegisterView(TemplateView):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)