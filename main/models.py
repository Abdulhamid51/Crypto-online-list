from django.db import models

# Create your models here.

class Coin(models.Model):
    name = models.CharField("Name", max_length=50)
    symbol = models.CharField("Symbol", max_length=50)
    price = models.FloatField("Price", default=0, blank=True)
    rank = models.IntegerField("Rank", default=0, blank=True)
    image = models.URLField("Image URL", max_length=1000, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['rank']