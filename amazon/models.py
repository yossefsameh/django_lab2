from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=10)
    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_cars(cls):
        return cls.objects.all()

    def get_show_url(self):
        return reverse("amazon.show",args=[self.id])

    def get_edit_url(self):
        return reverse("amazon.edit",args=[self.id])

    def get_delete_url(self):
        return reverse("amazon.delete",args=[self.id])
