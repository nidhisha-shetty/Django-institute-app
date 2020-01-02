from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields=[
			'Student_Rollno',
			'Student_Name',
			'Student_Class'
		]