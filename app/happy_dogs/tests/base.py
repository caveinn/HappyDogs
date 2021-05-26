from django.test import TestCase
from ..models import Dog, BoardingVisit
from django.utils import timezone
from .mock_data import dog_one, visit_one


# models test
class BaseTest(TestCase):

    def create_dog(self):
        dog = Dog(**dog_one)
        dog.save()
        return dog

    def create_boarding_visit(self):
        dog = self.create_dog()
        visit = BoardingVisit(**visit_one, dog=dog)
        visit.save()
        return visit
