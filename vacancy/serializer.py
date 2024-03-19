from rest_framework import serializers
from vacancy.models import Vacancy, Category, Subcategory


class VacancySerializer(serializers.ModelSerializer):
    image = serializers.StringRelatedField(source="company.image")
    district = serializers.StringRelatedField(source="address.title")
    region = serializers.StringRelatedField(source="address.region.title")

    class Meta:
        model = Vacancy
        fields = (
            "title",
            "district",
            "region",
            "salary",
            "phone",
            "image",
        )


class VacancyStatSerializer(serializers.Serializer):
    total_vacancy = serializers.IntegerField()
    total_company = serializers.IntegerField()
    total_resume = serializers.IntegerField()

    class Meta:
        model = Vacancy
        fields = (
            "total_vacancy",
            "total_company",
            "total_resume",
        )


class CategorySerializer(serializers.ModelSerializer):
    salary = serializers.CharField()
    # total_resume = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ("title", "salary", )
