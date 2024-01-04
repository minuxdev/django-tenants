from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class Lecture(models.Model):
    grade = models.ForeignKey(
        to=Grade,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lecture",
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
