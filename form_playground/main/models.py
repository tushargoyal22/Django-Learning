from django.db import models

# Create your models here.


class Student(models.Model):

    GENDERS=(
        ('F','Female'),
        ('M','Male')
    )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
