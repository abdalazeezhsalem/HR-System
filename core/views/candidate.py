from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Candidate
from ..serializers import CandidateSerializer


class CandidateAPIView(APIView):

    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        candidates = Candidate.objects.filter(pk=pk)
        serializer = CandidateSerializer(candidates, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        candidates = Candidate.objects.filter(pk=pk)
        candidates.delete()

