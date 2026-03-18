# quiz/urls.py

from django.urls import path
from .views import QuestionListView, QuizSubmitView, MyAnswersView, ResetQuizView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('submit/', QuizSubmitView.as_view(), name='quiz-submit'),
    path('my-answers/', MyAnswersView.as_view(), name='my-answers'),
    path('reset/', ResetQuizView.as_view(), name='quiz-reset'),
]
