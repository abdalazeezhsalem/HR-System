from django.contrib import admin

from .models.ScreeningResult import ScreeningResult
from .models.candidate import Candidate
from .models.InterviewQuestionSet import InterviewQuestionSet
from .models.resume import Resume
from .models.JobPosition import JobPosition ,RequiredSkill
from .models.department import Department
# Register your models here.


admin.site.register(InterviewQuestionSet)
admin.site.register(JobPosition)
admin.site.register(ScreeningResult)
admin.site.register(Department)
admin.site.register(Candidate)
admin.site.register(Resume)
admin.site.register(RequiredSkill)
