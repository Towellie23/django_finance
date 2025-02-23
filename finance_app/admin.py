from django.contrib import admin
from .models import *


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_at', 'end_at')
    filter = ('user',)

@admin.register(UserIncome)
class UserIncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'income', 'date')
    filter = ('user', 'date')


@admin.register(UserExpense)
class UserExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'expense', 'date')
    filter = ('user', 'date')


@admin.register(UserBudget)
class UserBudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'budget')
