from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Department
from ..serializers import DepartmentSerializer


@api_view(['GET', 'POST'])
def CreateDepartment(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def DepartmentView(request,pk):
    if request.method == 'GET':
        department = Department.objects.filter(pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        department = Department.objects.filter(pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        department = Department.objects.filter(pk=pk)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


