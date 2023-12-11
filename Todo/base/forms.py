from django import forms
from django.forms import ModelForm

from .models import Tasks

class TaskForm(forms.ModelForm):  # Capitalized TaskForm and Meta
    class Meta:  # Capitalized Meta
        model = Tasks
        fields = '__all__'
