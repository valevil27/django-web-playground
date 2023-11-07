from typing import Any
from django.db import models
from django.views.generic import ListView, DetailView
from registration.models import Profile


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"
    slug_url_kwarg = "username"
    slug_field = "user__username"