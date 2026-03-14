# quiz/models.py

from django.db import models
from users.models import CustomUser


class Question(models.Model):
    CATEGORY_CHOICES = [
        ('math', 'Matematika'),
        ('logic', 'Mantiq'),
        ('creative', 'Ijodkorlik'),
        ('social', 'Jamoa ishlash'),
        ('technical', 'Texnik'),
        ('interest', 'Qiziqishlar'),
    ]

    text = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.text[:50]}"


class UserAnswer(models.Model):
    SCORE_CHOICES = [
        (5, "Bu men haqimda!"),
        (4, "Ko'pincha shunday"),
        (3, "Ba'zida"),
        (2, "Kamdan-kam"),
        (1, "Bu men emasman"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(choices=SCORE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'question']

    def __str__(self):
        return f"{self.user.email} - {self.question.order} - {self.get_score_display()}"
