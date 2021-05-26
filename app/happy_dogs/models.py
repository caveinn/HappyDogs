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

    def save(self, *args, **kwargs):
        start_date_overlaps = self.dog.boardingvisit_set.filter(start_date__range=[self.start_date, self.end_date] ).exists()
        end_date_overlaps = self.dog.boardingvisit_set.filter(end_date__range=[self.start_date, self.end_date] ).exists()
        if not start_date_overlaps and not end_date_overlaps:
            return super().save(*args, **kwargs)
