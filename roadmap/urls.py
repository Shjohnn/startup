from django.urls import path
from .views import RoadmapView, SelectRoadmapView

urlpatterns = [
    path('roadmap/', RoadmapView.as_view(), name='roadmap'),
    path('roadmap/select/', SelectRoadmapView.as_view(), name='select-roadmap'),
]
