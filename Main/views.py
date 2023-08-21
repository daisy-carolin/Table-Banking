from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import User, Group, Contribution, Loan, LoanFunding, Interest, Fee, LoanExpenditure

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request, f"Your account has been created. You can log in now!"
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)


def home(request):
    return render (request, "dashboard.html")

def login_user(request):
    phone_number = request.POST.get("phone_number")
    password = request.POST.get("password")
    user = authenticate(request, phone_number=phone_number, password=password)
    print(user)
    if user is not None:
        print(f"User in role {user.role}")
        login(request, user)
        return redirect("dashboard")

    return render(request, "registration/login.html")



def logout(request):
    logout(request)
    return redirect("registration/login")

def join_group(request):
    return render(request, 'join_group.html')   

def add_member(request):
    return render(request, 'add_member.html') 

def member_contribution(request):
    return render(request, 'member_contribution.html') 

def group_set_up(request):
    return render(request, 'group_set_up.html') 


def create_group(request):
    records = CreateGroup.objects.all()
    
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_group")  
        else:
            print(form.errors)
    else:
        form = CreateGroupForm()  
        
    context = {"form": form, "records": records, "create_group": "active"}
    return render(request, "create_group.html", context)  



def contribute(request):
    records = Contribution.objects.all()
    form = ContributionForm(initial={"id": request.id})
    if request.method == "POST":
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contribute")
        else:
            print(form.errors)
    context = {"form": form, "records": records, "contribute": "active"}
    return render(request, "templates/contribute.html", context)


def request_loan(request):
    records = Loan.objects.all()
    form = LoanForm(initial={"id": request.id})
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("request_loan")
        else:
            print(form.errors)
    context = {"form": form, "records": records, "request_loan": "active"}
    return render(request, "templates/request_loan.html", context)


def fund_loan(request):
    records = LoanFunding.objects.all()
    form = LoanFundingForm(initial={"id": request.id})
    if request.method == "POST":
        form = LoanFundingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fund_loan")
        else:
            print(form.errors)
    context = {"form": form, "records": records, "fund_loan": "active"}
    return render(request, "templates/fund_loan.html", context)


def loan_expenditure(request):
    records = LoanExpenditure.objects.all()
    form = LoanExpenditureForm(initial={"id": request.id})
    if request.method == "POST":
        form = LoanExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loan_expenditure")
        else:
            print(form.errors)
    context = {"form": form, "records": records, "loan_expenditure": "active"}
    return render(request, "templates/loan_expenditure.html", context)





