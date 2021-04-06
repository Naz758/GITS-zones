from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Role(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("zones:zone-detail-view", args=[str(self.id)])

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    ext = models.CharField(
        "extension", help_text="eg.: 5068, 4563754, 4685051", max_length=25
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        return str(self.user)

    def get_absolute_url(self):
        return reverse("zones:profile-detail-view", args=[str(self.id)])

    def __str__(self):
        return str(self.user)


class Zone(models.Model):
    name = models.CharField(max_length=6)
    tech = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("zones:zone-detail-view", args=[str(self.id)])

    def __str__(self):
        return self.name


class Agency(models.Model):
    zone = models.ForeignKey(
        Zone, related_name="agency", on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "agencies"

    def get_absolute_url(self):
        return reverse("zones:agency-detail-view", args=[str(self.id)])

    def __str__(self):
        return self.name
