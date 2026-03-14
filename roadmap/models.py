from django.db import models
from users.models import CustomUser


class Roadmap(models.Model):
    FIELD_CHOICES = [
        ('backend', 'Backend Development'),
        ('frontend', 'Frontend Development'),
        ('data_science', 'Data Science'),
        ('ml', 'Machine Learning'),
        ('ai_engineering', 'AI Engineering'),
        ('flutter', 'Flutter Mobile'),
        ('android', 'Android Development'),
        ('ios', 'iOS Development'),
        ('devops', 'DevOps'),
        ('cybersecurity', 'Cybersecurity'),
        ('blockchain', 'Blockchain Development'),
        ('game_dev', 'Game Development'),
        ('ui_ux', 'UI/UX Design'),
        ('cloud', 'Cloud Engineering'),
        ('qa', 'QA / Testing'),
    ]

    field_name = models.CharField(max_length=50, choices=FIELD_CHOICES, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    total_hours = models.PositiveIntegerField()  # junior bo'lish uchun jami soat

    def __str__(self):
        return self.title


class RoadmapStep(models.Model):
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name='steps')
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    hours_needed = models.PositiveIntegerField()  # bu step uchun soat

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.roadmap.field_name} - {self.order}. {self.title}"


class UserRoadmap(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_roadmaps')
    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE)
    hours_per_day = models.PositiveIntegerField()  # kuniga necha soat
    selected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'roadmap']

    def __str__(self):
        return f"{self.user.email} - {self.roadmap.field_name}"
