from django import forms 
from main import models

class FormName(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    url = forms.URLField()
    text = forms.CharField(widget=forms.Textarea)
    
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = models.Student
        fields = '__all__'
