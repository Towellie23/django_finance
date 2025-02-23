from django.db import models
from django.contrib.auth.models import User

class UserIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.income} by {self.user.username} at {self.date}'

class UserExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.FloatField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'-{self.expense} by {self.user.username} at {self.date}'

class UserBudget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.FloatField()
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.budget} by {self.user.username} at {self.start_at}'

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.ManyToManyField(UserIncome)
    expense = models.ManyToManyField(UserExpense)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} report for {self.start_at} - {self.end_at}'