from django.db import models
from common.models import BaseModel, Region, District, Experience, WorkType


class Category(BaseModel):
    title = models.CharField(max_length=127, unique=True)

    def __str__(self):
        return self.title


class Subcategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoriya")
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=127, unique=True)
    image = models.ImageField(upload_to="images/company/")
    url = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return self.title


class Vacancy(BaseModel):
    title = models.CharField(max_length=127)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="kompaniya")
    address = models.ForeignKey(District, on_delete=models.CASCADE, related_name="manzil")

    experience = models.CharField(max_length=40, choices=Experience.choices, default=Experience.NO_EXPRERIENCE)
    work_type = models.CharField(max_length=20, choices=WorkType.choices, default=WorkType.DOIMIY)

    from_salary = models.PositiveIntegerField(default=0)
    until_salary = models.PositiveIntegerField(default=0, null=True, blank=True)

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="subcategoriya",
                                    null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    phone = models.PositiveIntegerField(default=901234567)

    def __str__(self):
        return self.title
