from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .forms import *
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'finance_app/index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'finance_app/signup.html', {'form': form})

@login_required
def dashboard(request):
    user_incomes = UserIncome.objects.filter(user=request.user)
    user_expenses = UserExpense.objects.filter(user=request.user)
    user_budgets = UserBudget.objects.filter(user=request.user)
    return render(request, 'finance_app/dashboard.html', {'user_incomes': user_incomes, 'user_expenses': user_expenses,
                                                          'user_budgets': user_budgets})


@login_required
def add_user_income(request):
    if request.method == 'POST':
        form = UserIncomeForm(request.POST)
        if form.is_valid():
            user_income = form.save(commit=False)
            user_income.user = request.user
            user_income.save()
            messages.success(request, 'Income added successfully')
            return redirect('finance_app/dashboard.html')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = UserIncomeForm()
    return render(request, 'finance_app/add_user_income.html', {'form': form})


@login_required
def add_user_expense(request):
    if request.method == 'POST':
        form = UserExpenseForm(request.POST)
        if form.is_valid():
            user_expense = form.save(commit=False)
            user_expense.user = request.user
            user_expense.save()
            messages.success(request, 'Expense added successfully')
            return redirect('finance_app/dashboard.html')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = UserExpenseForm()
    return render(request, 'finance_app/add_user_expense.html', {'form': form})


@login_required
def add_user_budget(request):
    if request.method == 'POST':
        form = UserBudgetForm(request.POST)
        if form.is_valid():
            user_budget = form.save(commit=False)
            user_budget.user = request.user
            user_budget.save()
            messages.success(request, 'Budget added successfully')
            return redirect('finance_app/dashboard.html')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = UserBudgetForm()
    return render(request, 'finance_app/add_user_budget.html', {'form': form})


@login_required
def edit_user_budget(request, pk):
    user_budget = get_object_or_404(UserBudget, pk=pk)
    if user_budget.user != request.user:
        return HttpResponseForbidden('У вас отсутствует доступ к данному бюджету')
    if request.method == 'POST':
        form = UserBudgetForm(request.POST, instance=user_budget)
        if form.is_valid():
            form.save()
            messages.success(request, 'Budget update successfully')
            return redirect('finance_app/user_budget_detail.html', pk=pk)
        else:
            messages.error(request, 'Invalid form')
    else:
        form = UserBudgetForm(instance=user_budget)
    return render(request, 'finance_app/edit_user_budget.html', {'form': form, 'user_budget': user_budget})

@login_required
def delete_user_budget(request, pk):
    user_budget = get_object_or_404(UserBudget, pk=pk)
    if user_budget.user != request.user:
        return HttpResponseForbidden('У вас отсутствует доступ к данному бюджету')
    if request.method == 'POST':
        user_budget.delete()
        messages.success(request, 'Budget delete successfully')
        return redirect('finance_app/delete_user_budget.html', {'user_budget': user_budget})

