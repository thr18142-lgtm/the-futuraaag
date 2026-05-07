from django import forms

from redapp.models import Student, College


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = "__all__"