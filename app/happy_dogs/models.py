from django.db import models

# Create your models here.

class Dog(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"



class BoardingVisit(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
