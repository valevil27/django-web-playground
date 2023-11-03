from django.urls import path
from .views import SignUpView

registration_patterns = ([
    path("sign_up/", SignUpView.as_view(), name="signup")
], "registration")