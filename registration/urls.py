from django.urls import path
from .views import SignUpView, ProfileView

registration_patterns = ([
    path("sign_up/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile"),
], "registration")