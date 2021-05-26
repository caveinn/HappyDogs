from django.db import models

# Create your models here.

class Dog(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ['first_name', 'last_name']

class BoardingVisit(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
