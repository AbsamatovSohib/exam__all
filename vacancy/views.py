from rest_framework import generics
from vacancy import models, serializer
from django.db.models import Count,  Max, Min, Avg, FloatField, Case, When, F, Value, ExpressionWrapper
from django.db.models.functions import Coalesce
from worker.models import Worker
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class VacancyListApiView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().select_related(
        "company", "address", "address__region")

    serializer_class = serializer.VacancySerializer


#keshlash
@method_decorator(cache_page(60*15), name="dispatch")
class VacancyStatisticView(generics.ListAPIView):
    queryset = models.Vacancy.objects.all().select_related("company")
    serializer_class = serializer.VacancyStatSerializer

    def get_queryset(self):

        total_vac = self.queryset.aggregate(total_vacancy=Count("title"))
        total_comp = {"total_company": self.queryset.values("company").distinct().count()}
        total_vac.update(total_comp)
        total_vac["total_resume"] = Worker.objects.all().count()

        return [total_vac]


@method_decorator(cache_page(60*15), name="dispatch")
class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.all().prefetch_related(
        "categoriya", "subcategoriya"
    )
    serializer_class = serializer.CategorySerializer

    def get_queryset(self):
        queryset = self.queryset.annotate(
            max_salary=Coalesce(Max(
                                    "categoriya__subcategoriya__until_salary"), 0),
            min_salary=Coalesce(Min(
                                    "categoriya__subcategoriya__from_salary"), 0),
            avg_salary=Coalesce(Avg(
                ExpressionWrapper(
                    F("categoriya__subcategoriya__from_salary")/2+F("categoriya__subcategoriya__until_salary")/2,
                    output_field=FloatField())), 0, output_field=FloatField())).values(
            "title", "max_salary", "min_salary", "avg_salary")

        queryset = queryset.annotate(
            salary=Case(When(
                    max_salary__lte=F("min_salary") * 2, then=ExpressionWrapper(
                        F("avg_salary"), output_field=FloatField())),
                        default=Value(0), output_field=FloatField()))

        for query in queryset:
            if query["max_salary"] >= 2*query["min_salary"]:
                price1 = (query["min_salary"] + query["avg_salary"])/2
                price2 = (query["max_salary"] + query["avg_salary"])/2

                query["salary"] = f"{price1} - {price2} UZS"
            else:
                query["salary"] = str(query["salary"])+" UZS"

        return queryset



