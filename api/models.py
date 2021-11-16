from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.CharField(max_length=400)
    description = models.TextField()
    stars = models.IntegerField()

    def __str__(self) -> str:
        return self.nam