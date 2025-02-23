from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import *
from .models import

router = DefaultRouter()

router.register('incomes', UserIncomeViewSet)
router.register('expenses', UserExpenseViewSet)
router.register('budgets', UserBudgetViewSet)
router.register('reports', ReportViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]