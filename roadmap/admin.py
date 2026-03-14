from django.contrib import admin
from .models import Roadmap, RoadmapStep, UserRoadmap


class RoadmapStepInline(admin.TabularInline):
    model = RoadmapStep
    extra = 1
    ordering = ['order']


@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ['field_name', 'title', 'total_hours']
    inlines = [RoadmapStepInline]


@admin.register(UserRoadmap)
class UserRoadmapAdmin(admin.ModelAdmin):
    list_display = ['user', 'roadmap', 'hours_per_day', 'selected_at']
