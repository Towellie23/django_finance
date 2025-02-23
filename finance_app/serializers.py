from rest_framework import serializers
from .models import UserIncome, UserBudget, UserExpense, Report


class UserIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIncome
        fields = '__all__'

class UserBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBudget
        fields = '__all__'

class UserExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExpense
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'