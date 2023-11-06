from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserWithMailCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Máximo 254 carácteres.")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def clean_email(self):
        # Get the email data from the form before sending   
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            # Validation error that prevents the form from sending the data
            raise forms.ValidationError("El email ya ha sido registrado.")
        return email
    
    
class ProfileForm(forms.ModelForm): 

    class Meta:
        model = Profile
        fields = ('avatar','bio','link')
        widgets = {
            "avatar": forms.ClearableFileInput(attrs = {
                'class': 'form-control-file mt-3'
            }),
            'bio': forms.Textarea(attrs= {'class':'form-control mt-1 mb-2', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs= {'class':'form-control mt-1 mb-2', 'placeholder':'Link'}),
        }