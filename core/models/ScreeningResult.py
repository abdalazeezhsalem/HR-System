# Fields:  ,  , , strengths , missing_skills ,
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Recommendation(models.TextChoices):
    PROCEED= 'PROCEED'
    REJECT = 'REJECT'
    HOLD = 'HOLD'


class ScreeningResult(models.Model):
    score = models.FloatField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    strengths = models.TextField(null=True,blank=True)
    missing_skills= models.TextField(null=True,blank=True)
    summary = models.TextField()
    raw_report= models.TextField()
    generated_at= models.DateTimeField(auto_now_add=True)
    recommendation=models.CharField(max_length=50,choices=Recommendation.choices, default=Recommendation.HOLD)


    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    job_position= models.ForeignKey('JobPosition', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate} - {self.job_position} ({self.recommendation})"