from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.
# title field
# purchaser field
# description field
# Register model with admin

class Snack(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    purchaser = models.CharField(max_length=64)
    description = models.TextField()


    def __str__(self):
        return self.name






    # def get_absolute_url(self):
    #     return reverse('detail_view', args=[str(self.id)])
    #     # return reverse('list_view')