from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer


@api_view(['POST'])
def CreateScreeningResult(request):
    if request.method == 'POST':
        serializer = ScreeningResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def ScreeningResultView(request,pk):
    if request.method == 'GET':
        screening_result = ScreeningResult.objects.filter(pk=pk)
        serializer = ScreeningResultSerializer(screening_result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        screening_result = ScreeningResult.objects.filter(pk=pk)
        serializer = ScreeningResultSerializer(screening_result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        screening_result = ScreeningResult.objects.filter(pk=pk)
        screening_result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


