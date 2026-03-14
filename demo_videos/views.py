from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .services import get_videos


class VideoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        field = request.query_params.get('field')

        if not field:
            return Response(
                {"error": "field parametri kerak. Masalan: ?field=backend"},
                status=status.HTTP_400_BAD_REQUEST
            )

        videos = get_videos(field)
        return Response(videos)

