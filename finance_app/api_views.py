from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import UserIncome, UserBudget, UserExpense, Report
from .serializers import UserIncomeSerializer, UserBudgetSerializer, UserExpenseSerializer, ReportSerializer


class UserIncomeViewSet(viewsets.ModelViewSet):
    queryset = UserIncome.objects.all()
    serializer_class = UserIncomeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserIncome.objects.all()
        return UserIncome.objects.filter(user=self.request.user)



class UserBudgetViewSet(viewsets.ModelViewSet):
    queryset = UserBudget.objects.all()
    serializer_class = UserBudgetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserBudget.objects.all()
        return UserBudget.objects.filter(user=self.request.user)


class UserExpenseViewSet(viewsets.ModelViewSet):
    queryset = UserExpense.objects.all()
    serializer_class = UserExpenseSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserExpense.objects.all()
        return UserExpense.objects.filter(user=self.request.user)

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAdminUser,)








