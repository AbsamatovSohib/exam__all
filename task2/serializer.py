from rest_framework import serializers
from task2 import models


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = ("title", "salary", )

