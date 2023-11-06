from django import forms
from django.contrib.auth.models import User
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import ProfileForm, UserWithMailCreationForm, EmailForm
from .models import Profile


# Create your views here.
class SignUpView(CreateView):
    form_class = UserWithMailCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_success_url(self) -> str:
        return super().get_success_url() + "?register"

    def get_form(
        self, form_class: type[BaseModelForm] | None = UserWithMailCreationForm
    ) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields["username"].widget = forms.TextInput(
            attrs={"class": "form-control mb-2", "placeholder": "Nombre de usuario"}
        )
        form.fields["email"].widget = forms.EmailInput(
            attrs={"class": "form-control mb-2", "placeholder": "Email"}
        )
        form.fields["password1"].widget = forms.PasswordInput(
            {"class": "form-control mb-2", "placeholder": "Contraseña"}
        )
        form.fields["password2"].widget = forms.PasswordInput(
            {"class": "form-control mb-2", "placeholder": "Repite tu contraseña"}
        )
        return form

@method_decorator(login_required, name="dispatch")
class ProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("registration:profile")
    template_name = "registration/profile_form.html"
    
    #? How to get the object that we want to update
    def get_object(self, queryset= None) -> Profile:
        profile, created = Profile.objects.get_or_create(user = self.request.user)
        return profile
    
class EmailUpdateView(UpdateView):
    model = User
    template_name = "registration/profile_email_form.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy("registration:profile") + "?email"

    def get_object(self, queryset= None) -> User:
        user = self.request.user
        return user # type: ignore
    # Now we overwrite the form widget in execution time
    def get_form(self, form_class = EmailForm):
        form = super().get_form(form_class)
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control','placeholder':"Email"}
        )
        return form