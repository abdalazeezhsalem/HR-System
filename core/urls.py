from django.urls import path

from .views import (DepartmentView , CandidateAPIView , JobPositionView
, CreateJobPosition ,ResumeView ,UploadResume ,ScreeningResultView,CreateScreeningResult , CreateInterviewQuestionSet ,InterviewQuestionSetView)

# ,InterviewQuestionSet



urlpatterns = [

    path('department/', DepartmentView,name='department'),

    path('candidate/',CandidateAPIView.as_view(),name='candidate'),

    path('job_position/',CreateJobPosition,name='job_position'),
    path('job_position/<int:pk>/',JobPositionView,name='job_position'),

    path('resume/<int:candidate>/',ResumeView,name='resume'),
    path('upload_resume/',UploadResume,name='upload_resume'),

    path('create_result/',CreateScreeningResult,name='create_result'),
    path('result_view/<int:pk>/', ScreeningResultView, name='result_view'),

    path('create_InterviewQuestionSet/',CreateInterviewQuestionSet,name='create_InterviewQuestionSet'),
    path('InterviewQuestionSet_view/<int:pk>/', ScreeningResultView, name='InterviewQuestionSet_view'),

]