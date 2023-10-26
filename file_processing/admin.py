from django.contrib import admin

# Register your models here.
from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Данные о файле",
            {
                "fields": ('file', 'uploaded_at', 'processed',),
                "classes": ('wide',),
            }
        ),
    ]
    list_display = [
        'file',
        'uploaded_at',
        'processed',
    ]
    search_fields = 'file',
