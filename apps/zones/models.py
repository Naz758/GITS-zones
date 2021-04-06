from django.db import models
from django.urls import reverse


class Zone(models.Model):
    name = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("zones:zone-detail-view", args=[str(self.id)])

    def __str__(self):
        return self.name


class Agency(models.Model):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "agencies"

    def __str__(self):
        return self.name
