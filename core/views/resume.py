from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Resume
from ..serializers import ResumeSerializer


@api_view(['GET', 'POST'])
def UploadResume(request):
    if request.method == 'GET':
        resume = Resume.objects.all()
        serializer = ResumeSerializer(resume, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def ResumeView(request,candidate):


    if request.method == 'PUT':
        resume = Resume.objects.filter(candidate=candidate)
        serializer = ResumeSerializer(resume, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':
        resume = Resume.objects.filter(candidate=candidate)
        resume.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        resume = Resume.objects.filter(candidate=candidate)
        serializer = ResumeSerializer(resume, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


