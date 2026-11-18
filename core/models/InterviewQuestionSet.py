from django.db import models


class InterviewQuestionSet(models.Model):
    generated_at= models.DateTimeField(auto_now_add=True)
    follow_up_questions=models.JSONField(default=list, blank=True)
    behavioral_questions=models.JSONField(default=list, blank=True)
    technical_question= models.JSONField(default=list ,blank=True)


    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    job_position = models.ForeignKey('JobPosition', on_delete=models.CASCADE)
    screening_result= models.ForeignKey('ScreeningResult', on_delete=models.CASCADE)

    def __str__(self):
        return f'Questions for {self.candidate} - {self.job_position}'