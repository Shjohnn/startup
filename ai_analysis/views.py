from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from quiz.models import UserAnswer
from .services import analyze_answers
from .serializers import AnalysisResultSerializer


class AnalyzeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        answers = UserAnswer.objects.filter(
            user=request.user
        ).select_related('question')

        if not answers.exists():
            return Response(
                {"error": "Avval quizni to'ldiring!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        results = analyze_answers(request.user, answers)
        serializer = AnalysisResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

