# quiz/serializers.py

from rest_framework import serializers
from .models import Question, UserAnswer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'category', 'order']


class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['question', 'score']


class QuizSubmitSerializer(serializers.Serializer):
    answers = UserAnswerSerializer(many=True)

    def validate_answers(self, answers):
        # if len(answers) != 40:
        #     raise serializers.ValidationError("40 ta javob bo'lishi kerak")
        return answers

    def save(self, user):
        answers = self.validated_data['answers']
        objs = [
            UserAnswer(
                user=user,
                question=a['question'],
                score=a['score']
            )
            for a in answers
        ]
        UserAnswer.objects.bulk_create(objs, ignore_conflicts=True)
