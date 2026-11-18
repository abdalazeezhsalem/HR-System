from django.db import models

from ..models import Department


class RequiredSkill(models.Model):
    title = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.title


class JobPosition(models.Model):

    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='job_position')
    title = models.TextField()
    description = models.TextField()


    required_skills = models.ManyToManyField('RequiredSkill',related_name='job_positions')

    def __str__(self):
        return self.title