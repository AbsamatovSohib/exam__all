from task2 import models, serializer, filter
from rest_framework import generics


class VacancyFilterView(generics.ListAPIView):
    queryset = models.Job.objects.all()
    serializer_class = serializer.VacancySerializer

    filterset_class = filter.MyFilter

