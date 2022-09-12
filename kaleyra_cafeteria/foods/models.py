from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Breakfast(models.Model):
    date = models.DateField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField(User, blank=True)
    price = models.FloatField()
    image = models.URLField(max_length=1000,
                            default="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YnVyZ2VyfGVufDB8fDB8fA%3D%3D&w=1000&q=80")

    class Meta:
        ordering = 'date',
        verbose_name_plural = 'Breakfast'

    def __str__(self):
        return self.title


class Snacks(models.Model):
    date = models.DateField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField(User, blank=True)
    price = models.FloatField()
    image = models.URLField(max_length=1000,
                            default="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YnVyZ2VyfGVufDB8fDB8fA%3D%3D&w=1000&q=80")

    class Meta:
        ordering = 'date',
        verbose_name_plural = 'Snacks'

    def __str__(self):
        return self.title
