from django.forms import ModelForm
from django import forms
from main.models import Student
class UploadForm(ModelForm):
    limage=forms.ImageField(label="Upload left eye image\n")
    rimage=forms.ImageField(label="Upload right eye image")
    class Meta:
        model=Student
        fields=['limage','rimage']