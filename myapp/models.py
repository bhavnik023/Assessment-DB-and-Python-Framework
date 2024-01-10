from django.db import models

# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="")
	profile_image=models.ImageField(default="",upload_to="profile_image/")
	
	def __str__(self):
		return self.fname

