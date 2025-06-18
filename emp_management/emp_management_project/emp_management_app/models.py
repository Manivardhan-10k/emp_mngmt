from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    contact = models.CharField(max_length=15, default='0000000000') 
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, default='Not Assigned')
    profile_image = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

