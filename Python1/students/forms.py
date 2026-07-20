from django import forms
from .models import Student
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(role='Student'),
        empty_label="Select a student",
    )
    class Meta:
        model = Student
        fields = [
           'dob',
           'gender',
           'cgpa',
           'photo',
           'department',
           'courses',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'courses': forms.CheckboxSelectMultiple(),
        }
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("A student with this email already exists.")
            return email
        def clean_cgpa(self):
            cgpa = self.cleaned_data.get('cgpa')
            if cgpa < 0 or cgpa > 10:
                raise forms.ValidationError("CGPA must be between 0 and 10.")
            return cgpa