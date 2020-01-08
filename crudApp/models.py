from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Student(models.Model):
    course_choices = [('python', 'Python'), ('java', 'Java'),
                      ('django', 'Django'), ('flask', 'Flask')]
    fullname = models.CharField(max_length=20)
    course = models.CharField(max_length=10, choices=course_choices)
    fee = models.FloatField()

    def __repr__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('cbv_student_detail', kwargs={'pk': self.pk})
