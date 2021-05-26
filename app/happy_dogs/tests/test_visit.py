from .base import BaseTest
from ..models import BoardingVisit

class BoardinVisitTest(BaseTest):
    def test_create_visit(self):
        visit = self.create_boarding_visit()
        self.assertIsInstance(visit, BoardingVisit)

    def test_fetch_home(self):
        resp = self.fetch_home_view()
        self.assertEqual(resp.status_code , 200)

    def test_fetch_home(self):
        resp = self.fetch_home_view()
        self.assertEqual(resp.status_code , 200)

    def test_fetch_boarding_visits(self):
        resp = self.fetch_boarding_visit()
        self.assertEqual(resp.status_code , 200)
        self.assertIn('Dog'.encode(), resp.content)
