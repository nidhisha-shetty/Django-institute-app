from django.db import models
from django.urls import reverse


# Create your models here.

class Student(models.Model):
	Student_Rollno=models.CharField(max_length=100)
	Student_Name=models.CharField(max_length=100)
	Student_Class=models.CharField(max_length=100)

	def get_absolute_url(self):
			
		return reverse("student-details-display-id", kwargs={"my_id":self.id})
			#return f"/student/{self.id}/"

	def get_absolute_url_edit(self):
		#return f"/article_edit/{self.id}/"
		return reverse("student-edit-id", kwargs={"my_id":self.id})

	def get_absolute_url_delete(self):
		#return f"/article_edit/{self.id}/"
		return reverse("student-details-delete-id", kwargs={"my_id":self.id})