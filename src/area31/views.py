from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Location, LocationLabel
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.utils.functional import cached_property
from .forms import ProfileForm, UserUpdateForm, LocationRegisterForm

@login_required
def remove_location(request):
    if request.method == "POST":
        location_id = request.POST["location_id"]
        Location.objects.filter(id=location_id).delete()
        return redirect("profile")

@login_required
def register_location(request):

    if request.method == "POST":

        location_form = LocationRegisterForm(request.POST or None)

        # if location_form.is_valid():
        location = location_form.save(commit=False)
        location.user = request.user
        location.save()

        return redirect("map")

    else:
        location_form = LocationRegisterForm()
        context = {
            "get_locations": Location.objects.all(),
            "location_form" : location_form
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

        print(request.FILES)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        # if user_form.is_valid() and profile_form.is_valid():
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