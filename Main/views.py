from multiprocessing import context
from django.contrib import messages
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
    groups = CreateGroup.objects.all()
    context= {"groups":groups}    
    return render(request, 'join_group.html', context)
  
    
def add_member(request):
    if request.method == "POST":
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the appropriate URL after successful form submission
    else:
        form = MembershipForm()
    
    context = {"form": form}
    return render(request, 'add_member.html', context)

def delete_member(request, pk):  # Updated parameter name
    try:
        member = Member.objects.get(pk=pk)  # Using 'pk' as the parameter
        if request.method == 'POST':
            member.delete()  # Delete the member
            return redirect('dashboard')
    except Member.DoesNotExist:
        # Handle the case where the member doesn't exist
        pass
    return render(request, 'delete_member.html', {'member': member})   # Render a delete confirmation page
    
from django.shortcuts import get_object_or_404
from .models import UserGroupMembership, Group

# def join_specific_group(request, id):
#     if request.user.is_authenticated:
#         group = get_object_or_404(CreateGroup, id=id)  # Get the group by ID
#         membership = UserGroupMembership(user=request.user, group=group)
#         membership.save()
#         return render(request, 'joined_group.html', {'group': group})
#         print("Hello Shama")
#     else:
#         # Redirect the user to the login page or show an appropriate message
#         return redirect('home')
#         pass
from django.shortcuts import get_object_or_404, render, redirect
from .models import CreateGroup, UserGroupMembership

def join_specific_group(request, id):
    if request.user.is_authenticated:
        group = get_object_or_404(CreateGroup, id=id)  # Get the group by ID

        try:
            membership = UserGroupMembership(user=request.user, group=group)
            membership.save()
            group_joined = True
        except Exception as e:
            group_joined = False
            # Print or log the error message for debugging
            print(f"Error joining group: {e}")

        return render(request, 'joined.html', {'group': group, 'group_joined': group_joined})
    else:
        # Redirect the user to the login page or show an appropriate message
        return redirect('home')


def member_contribution(request):
    return render(request, 'member_contribution.html') 

def group_set_up(request):
    return render(request, 'group_set_up.html') 


def member_list(request):
    members = Member.objects.all()  # Get all members from the database
    return render(request, 'member_list.html', {'members': members})


def group_members(request, group_id):
    group = Group.objects.get(id=group_id)  # Get the group by ID
    members = Member.objects.filter(usergroupmembership__group=group)
    return render(request, 'group_members.html', {'group': group, 'members': members})


def create_group(request):
    if request.method == "POST":
        form = CreateGroupForm(request.POST)
        
        if form.is_valid():
            group = form.save()
            print("Group Created for:", group)
            messages.success(request, "Group created successfully!")
            return redirect('dashboard')
        else:
            print(form.errors)
            messages.error(request, "There were errors in the form.")
    else:
        form = CreateGroupForm()

    context = {"form": form, "create_group": "active"}
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
    
