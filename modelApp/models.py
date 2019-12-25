from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_num = models.IntegerField()
    address = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=30)
    salary = models.IntegerField()
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    number_type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    progrmmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)


class License(models.Model):
    license_type = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    valid_until = models.DateField()
    valid_from = models.DateField(auto_now_add=True)
    programmer = models.OneToOneField(Programmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
