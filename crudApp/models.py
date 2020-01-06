from django.db import models

# Create your models here.


class Student(models.Model):
    course_choices = [('python', 'Python'), ('java', 'Java'),
                      ('django', 'Django'), ('flask', 'Flask')]
    fullname = models.CharField(max_length=20)
    course = models.CharField(max_length=10, choices=course_choices)
    fee = models.FloatField()

    def __repr__(self):
        return self.fullname
