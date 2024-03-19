import django_filters
from task2.models import Job


class MyFilter(django_filters.FilterSet):
    salary_from = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_to = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='exact')

    class Meta:
        model = Job
        fields = ("salary", "salary_from", "salary_to")
