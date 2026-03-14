from django.contrib import admin
from .models import AnalysisResult


@admin.register(AnalysisResult)
class AnalysisResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'field_name', 'percentage', 'created_at']
    list_filter = ['field_name']
