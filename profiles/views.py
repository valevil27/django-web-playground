from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from registration.models import Profile


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    paginate_by =9


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"
    
    def get_object(self, queryset = None) -> Profile:
        username = self.kwargs.get('username')
        profile = get_object_or_404(Profile, user__username= username)
        return profile