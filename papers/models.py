from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Paper(models.Model):
    title = models.CharField(max_length=300)
    journal = models.CharField(max_length=100)
    authors = models.CharField(max_length=70)
    abstract = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title


