from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Roadmap, UserRoadmap
from .serializers import RoadmapSerializer, UserRoadmapSerializer


class RoadmapView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        field = request.query_params.get('field')
        hours_per_day = int(request.query_params.get('hours_per_day', 2))

        if not field:
            return Response(
                {"error": "field parametri kerak. Masalan: ?field=data_science&hours_per_day=2"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            roadmap = Roadmap.objects.get(field_name=field)
        except Roadmap.DoesNotExist:
            return Response(
                {"error": f"{field} uchun roadmap topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RoadmapSerializer(
            roadmap,
            context={'hours_per_day': hours_per_day}
        )
        return Response(serializer.data)


class SelectRoadmapView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        field = request.data.get('field')
        hours_per_day = request.data.get('hours_per_day', 2)

        try:
            roadmap = Roadmap.objects.get(field_name=field)
        except Roadmap.DoesNotExist:
            return Response(
                {"error": "Roadmap topilmadi"},
                status=status.HTTP_404_NOT_FOUND
            )

        user_roadmap, created = UserRoadmap.objects.update_or_create(
            user=request.user,
            roadmap=roadmap,
            defaults={'hours_per_day': hours_per_day}
        )

        serializer = RoadmapSerializer(
            roadmap,
            context={'hours_per_day': hours_per_day}
        )
        return Response({
            "message": "Yo'nalish tanlandi!",
            "roadmap": serializer.data
        }, status=status.HTTP_201_CREATED)
