from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    class Meta:
        abstract = True


class Region(models.Model):
    title = models.CharField(max_length=127)

    def __str__(self):
        return self.title


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="regions")
    title = models.CharField(max_length=127)

    def __str__(self):
        return self.title


class Experience(models.TextChoices):
    NO_EXPRERIENCE = "no experience",
    UNTILL_ONE = "until one year",
    FROM_ONE_UNTILL_TWO = "from one until two years",
    FROM_TWO_UNTILL_FIVE = "from two untill five years",
    FROM_FIVE_UNTILL_TEN = "from five until ten years",
    MORE_TEN = "more than ten years",


class WorkType(models.TextChoices):
    DOIMIY = "domimiy bandlik",
    YARIM_KUNLIK = "yarim kunlik",
    MOSLASHUVCHAN = "moslashuvchan grafik",
