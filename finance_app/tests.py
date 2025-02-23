from django.test import TestCase
from .models import *
from rest_framework.test import APIClient


class UserIncomeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='TestIvan', password='789456123TestIvan')
        self.admin = User.objects.create_superuser(username='AdminIvan', password='789456123AdminIvan')
        self.income = UserIncome.objects.create(
            user=self.user,
            income='5000.20',
            description='Trading test',
        )
        self.client = APIClient()

    def test_user_income(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/incomes/{self.income.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Trading test')

    def test_unauthorized_access(self):
        response = self.client.get(f'/api/incomes/{self.income.id}/')
        self.assertEqual(response.status_code, 403)

    def test_redirect_to_login(self):
        self.client.logout()
        response = self.client.get(f'/api/incomes/{self.income.id}/')
        self.assertEqual(response.status_code, 403)