from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(forms.ModelForm):
    student_name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name'}))
    student_class = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
    radiobutton = [('male','Male'),('female','Female')]
    student_gender = forms.ChoiceField(widget= forms.RadioSelect, choices=radiobutton)
    checkbox = [('physics','Physics'),('chemistry','Chemistry'),('maths','Maths'),('all','All')]

    student_subject = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=checkbox)
    student_enrollment_id = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'placeholder': 'Enter Enrollment Id'}))
    class Meta:
        model = Student
        fields = '__all__'
