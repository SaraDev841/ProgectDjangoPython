from django import forms
from .models import Task ,UserProfile ,User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','desc','destDate','status','performer']
        widgets = {
            'destDate': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'team': forms.HiddenInput()
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role','team']




