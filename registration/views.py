from django import forms
from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserWithMailCreationForm


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
