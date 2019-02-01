from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Location
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.utils.functional import cached_property
from .forms import ProfileForm, UserUpdateForm


@login_required
def register_profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST or None, instance=request.user)
        profile_form = ProfileForm(request.POST or None, instance=request.user.profile)

        user = user_form.save(commit=False)
        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        return redirect("profile")

    else:
        context = {
            "get_users": User.objects.all(),
            "get_locations": Location.objects.all(),
        }
        return render(request, 'map.html', context)


@method_decorator(login_required, name='dispatch')
class UserListView(TemplateView):
    template_name = "users.html"

    @cached_property
    def get_users(self):
        return User.objects.filter(is_superuser=False)

    def get(self, request, *args, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)


@login_required
def edit_profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST or None, instance=request.user)
        profile_form = ProfileForm(request.POST or None, instance=request.user.profile)

        user = user_form.save(commit=False)
        user.save()

        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        return redirect("profile")

    else:
        parsonl_locations = Location.objects.filter(user=request.user)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {
            "user_form": user_form,
            "profile_form": profile_form,
            "parsonal_locations" : parsonl_locations
        }
        return render(request, 'profile.html', context)