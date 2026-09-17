from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student   #this form is connected to Student model
        fields = ['name', 'email', 'age', 'address']