# quiz/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Question, UserAnswer
from .serializers import QuestionSerializer, QuizSubmitSerializer


class QuestionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class QuizSubmitView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = QuizSubmitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"message": "Javoblar saqlandi!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyAnswersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = UserAnswer.objects.filter(user=request.user).count()
        return Response({'count': count})


class ResetQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        UserAnswer.objects.filter(user=request.user).delete()
        return Response({"message": "Test qayta boshlash uchun tayyor!"})
