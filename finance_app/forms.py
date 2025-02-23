from django import forms
from .models import *


class UserIncomeForm(forms.ModelForm):
    class Meta:
        model = UserIncome
        fields = ['income', 'description']


class UserExpenseForm(forms.ModelForm):
    class Meta:
        model = UserExpense
        fields = ['description', 'expense']


class UserBudgetForm(forms.ModelForm):
    class Meta:
        model = UserBudget
        fields = ['budget']


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['income', 'expense']


