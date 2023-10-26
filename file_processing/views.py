from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            instance = serializer.save()
            process_file.delay(instance.id)


@api_view(['POST'])
def upload_file(request):
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        process_file.delay(request.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
