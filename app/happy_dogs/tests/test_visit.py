from .base import BaseTest
from ..models import BoardingVisit

class BoardinVisitTest(BaseTest):
    def test_create_visit(self):
        visit = self.create_boarding_visit()
        self.assertIsInstance(visit, BoardingVisit)
