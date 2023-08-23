from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from .models import Contribution, Loan, LoanFunding, Interest, Fee, LoanExpenditure,LoanFunding, LoanRepayment

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

def borrow_loan(request):
    return render(request, 'borrow_loan.html')

def repay_loan(request):
    return render(request, 'repay_loan.html')

def loan_repayment(request):
    return render(request, 'loan_repayment.html')


# @login_required
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

# @login_required
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

# @login_required
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


# @login_required
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





# # @login_required
# def borrow_loan(request):
#     user = request.user

#     if request.method == 'POST':
#         # Handle loan borrowing
#         loan_amount = float(request.POST.get('loan_amount', 0))
#         if user.balance >= loan_amount:
#             loan = Loan.objects.create(
#                 user=user,
#                 amount=loan_amount,
#                 remaining_amount=loan_amount,
#                 is_repaid=False,
#                 is_approved=False
#             )
#             user.balance -= loan_amount
#             user.save()
#             return redirect('borrow_loan')

#     return render(request, 'borrow_loan.html')

# # @login_required
# def fund_loan(request, loan_id):
#     loan = Loan.objects.get(id=loan_id)
#     user = request.user

#     if request.method == 'POST':
#         # Handle loan funding
#         funding_amount = float(request.POST.get('funding_amount', 0))
#         if user.balance >= funding_amount:
#             LoanFunding.objects.create(user=user, loan=loan, amount_funded=funding_amount)
#             user.balance -= funding_amount
#             user.save()
#             return redirect('fund_loan', loan_id=loan_id)

#     return render(request, 'fund_loan.html', {'loan': loan})

# # @login_required
# def repay_loan(request, loan_id):
#     loan = Loan.objects.get(id=loan_id)
#     user = request.user

#     if request.method == 'POST':
#         # Handle loan repayment
#         repayment_amount = float(request.POST.get('repayment_amount', 0))
#         if user.balance >= repayment_amount:
#             LoanRepayment.objects.create(loan=loan, amount=repayment_amount)
#             loan.remaining_amount -= repayment_amount
#             if loan.remaining_amount <= 0:
#                 loan.is_repaid = True
#             loan.save()
#             user.balance -= repayment_amount
#             user.save()
#             return redirect('repay_loan', loan_id=loan_id)

#     return render(request, 'repay_loan.html', {'loan': loan})





