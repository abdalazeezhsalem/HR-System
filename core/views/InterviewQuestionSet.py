from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer



@api_view(['GET', 'POST'])
def CreateInterviewQuestionSet(request):
    if request.method == 'GET':
        interview_questionSet = InterviewQuestionSet.objects.all()
        serializer = InterviewQuestionSetSerializer(interview_questionSet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = InterviewQuestionSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def InterviewQuestionSetView(request,pk):
    if request.method == 'GET':
        interview_questionSet = InterviewQuestionSetView.objects.filter(pk=pk)
        serializer = InterviewQuestionSetSerializer(interview_questionSet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        interview_questionSet = InterviewQuestionSetView.objects.filter(pk=pk)
        serializer = InterviewQuestionSetSerializer(interview_questionSet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        interview_questionSet = InterviewQuestionSet.objects.filter(pk=pk)
        interview_questionSet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















