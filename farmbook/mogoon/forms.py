from django import forms
from .models import Crop, Fertilizer, Kandojobs, Milk


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


class UpdateFertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = '__all__'


class UpdateKandojobsForm(forms.ModelForm):
    class Meta:
        model = Kandojobs
        fields = '__all__'


class UpdateMilkForm(forms.ModelForm):
    class Meta:
        model = Milk
        fields = '__all__'
