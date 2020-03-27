from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=100)
    band = models.ForeignKey(Band, models.CASCADE)

    def __str__(self):
        return self.name
