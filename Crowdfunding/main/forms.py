from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =  ['naziv','opis','pocetak_kampanje','zavrsetak_kampanje','ciljani_iznos','trenutni_iznos', 'autor']
        widgets = {
            'pocetak_kampanje': forms.DateInput(attrs={'type': 'date'}),
            'zavrsetak_kampanje': forms.DateInput(attrs={'type': 'date'})
        }
        