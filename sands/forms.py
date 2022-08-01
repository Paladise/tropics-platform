from django import forms
from .models import SandTeacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = SandTeacher
        fields = ["display_name", "fcps_email"]
        
        labels = {
            "display_name": "",
            "fcps_email": ""
        }
        
        widgets = {
            "display_name": forms.TextInput(attrs={'placeholder': 'Name'}),
            "fcps_email": forms.EmailInput(attrs={'placeholder': 'Email (Optional)'})
        }