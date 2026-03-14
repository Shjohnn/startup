# quiz/urls.py

from django.urls import path
from .views import QuestionListView, QuizSubmitView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('submit/', QuizSubmitView.as_view(), name='quiz-submit'),
]

