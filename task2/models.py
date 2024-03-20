from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=64)
    salary = models.PositiveIntegerField()
    # salary_from = models.PositiveIntegerField()
    # salary_until= models.PositiveIntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title
