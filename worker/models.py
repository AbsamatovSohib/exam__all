from django.db import models
from common.models import BaseModel, District
from vacancy.models import Subcategory, Experience
from django.contrib.auth import get_user_model

User = get_user_model()


class Worker(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_worker")
    full_name = models.CharField(max_length=127)
    info = models.TextField()
    address = models.ForeignKey(District, on_delete=models.CASCADE, related_name="tuman")

    profession = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="pro")

    salary = models.PositiveIntegerField()
    experience = models.CharField(choices=Experience.choices, default=Experience.NO_EXPRERIENCE, max_length=50)

    def __str__(self):
        return self.full_name


