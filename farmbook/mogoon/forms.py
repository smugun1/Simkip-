from django import forms
from .models import Crop


class TaskForm(forms.ModelForm):
    content = forms.CharField(label='BuildGreen', widget=forms.TextInput(
        attrs={'placeholder': 'Add task here...'}))

    class Meta:
        model = Crop
        fields = '__all__'


class UpdateTaskForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = '__all__'
