from celery import shared_task
from rest_framework import status
from rest_framework.response import Response

from .handlers import get_file_type
from .models import File
from .serializers import FileSerializer

malicious_files = [
    'php', 'js', 'exe',
    'application', 'msi',
    'msp', 'pif', 'com',
    'jar', 'hta', 'vbs'
]


@shared_task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        serializer = FileSerializer(file)
        if get_file_type(file.file) not in malicious_files:
            file.processed = True
            file.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            file.delete()
            return Response({"message": "Вредоносный файл! Такие не принимаем!"}, status=status.HTTP_400_BAD_REQUEST)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
