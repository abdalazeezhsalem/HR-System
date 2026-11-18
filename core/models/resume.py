from django.db import models
from django.core.validators import FileExtensionValidator


class Resume(models.Model):
    candidate=models.OneToOneField('Candidate',on_delete=models.CASCADE)
    file=models.FileField(upload_to='resumes',validators=[FileExtensionValidator(['PDF','DOC','TXT'])])
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"{self.candidate} - {self.file.name}"