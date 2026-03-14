from django.db import models
from users.models import CustomUser


class AnalysisResult(models.Model):
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

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='results')
    field_name = models.CharField(max_length=50, choices=FIELD_CHOICES)
    percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-percentage']

    def __str__(self):
        return f"{self.user.email} - {self.field_name} - {self.percentage}%"
