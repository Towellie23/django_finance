from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import *
from .models import *
from .views import *

router = DefaultRouter()

router.register('incomes', UserIncomeViewSet)
router.register('expenses', UserExpenseViewSet)
router.register('budgets', UserBudgetViewSet)
router.register('reports', ReportViewSet)

app_name = 'finance_app'

urlpatterns = [
    path('api/', include(router.urls)),
    path('add_user_budget/', add_user_budget, name='add_user_budget'),
    path('add_user_income/', add_user_income, name='add_user_income'),
    path('add_user_expense/', add_user_expense, name='add_user_expense'),
    path('delete_user_budget/<int:pk>/', delete_user_budget, name='delete_user_budget'),
    path('edit_user_budget/<int:pk>/', edit_user_budget, name='edit_user_budget'),
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),

]