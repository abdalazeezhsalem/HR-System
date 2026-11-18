from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import JobPosition
from ..serializers import JobPositionSerializer


@api_view(['GET', 'POST'])
def CreateJobPosition(request):
    if request.method == 'GET':
        job_positions = JobPosition.objects.all()
        serializer = JobPositionSerializer(job_positions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = JobPositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def JobPositionView(request,pk):
    if request.method == 'GET':
        job_position = JobPosition.objects.filter(pk=pk)
        serializer = JobPositionSerializer(job_position, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        jpb_position = JobPosition.objects.filter(pk=pk)
        serializer = JobPositionSerializer(jpb_position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job_position = JobPosition.objects.filter(pk=pk)
        job_position.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


