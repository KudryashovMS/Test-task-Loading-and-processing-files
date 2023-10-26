from django.urls import path

from .views import (
    FileUploadView,
    upload_file,
    FileListView,
)

urlpatterns = [
    path("upload/", upload_file, name="upload"),
    path("upload1/", FileUploadView.as_view(), name="upload1"),
    path("files/", FileListView.as_view(), name="files"),
]