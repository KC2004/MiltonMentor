from django import forms

from .models import User

class CreateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('job_function', 'job_industry','major_study','city_location')

        