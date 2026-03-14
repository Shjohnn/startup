from rest_framework import serializers
from .models import Roadmap, RoadmapStep, UserRoadmap


class RoadmapStepSerializer(serializers.ModelSerializer):
    days_needed = serializers.SerializerMethodField()

    class Meta:
        model = RoadmapStep
        fields = ['order', 'title', 'description', 'hours_needed', 'days_needed']

    def get_days_needed(self, obj):
        hours_per_day = self.context.get('hours_per_day', 2)
        days = obj.hours_needed / hours_per_day
        return round(days)


class RoadmapSerializer(serializers.ModelSerializer):
    steps = serializers.SerializerMethodField()
    total_days = serializers.SerializerMethodField()
    total_weeks = serializers.SerializerMethodField()
    total_months = serializers.SerializerMethodField()

    class Meta:
        model = Roadmap
        fields = ['field_name', 'title', 'description', 'total_hours',
                  'total_days', 'total_weeks', 'total_months', 'steps']

    def get_steps(self, obj):
        hours_per_day = self.context.get('hours_per_day', 2)
        serializer = RoadmapStepSerializer(
            obj.steps.all(),
            many=True,
            context={'hours_per_day': hours_per_day}
        )
        return serializer.data

    def get_total_days(self, obj):
        hours_per_day = self.context.get('hours_per_day', 2)
        return round(obj.total_hours / hours_per_day)

    def get_total_weeks(self, obj):
        return round(self.get_total_days(obj) / 7)

    def get_total_months(self, obj):
        return round(self.get_total_days(obj) / 30)


class UserRoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoadmap
        fields = ['roadmap', 'hours_per_day']
