from django.contrib import admin
from .models import Question, UserAnswer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['order', 'text', 'category']
    list_filter = ['category']
    ordering = ['order']


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'score']
