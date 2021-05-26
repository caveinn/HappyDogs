from .base import BaseTest
from ..models import Dog
from django.db.utils import IntegrityError

class DogTest(BaseTest):
    def test_create_dog(self):
        dog = self.create_dog()
        self.assertIsInstance(dog, Dog)

    def test_dog_cannot_create_duplicatie(self):
        self.create_dog()
        with self.assertRaises(IntegrityError):
            self.create_dog()

