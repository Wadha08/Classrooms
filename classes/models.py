from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	Teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})

class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	FEMALE = 'Female'
	MALE = 'Male'
	gender_choices=[(FEMALE,'Female'),(MALE,'Male')]
	gender = models.CharField(max_length=7,choices=gender_choices,default=FEMALE)
	exam_grade = models.DecimalField(max_digits=10, decimal_places=3)
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


