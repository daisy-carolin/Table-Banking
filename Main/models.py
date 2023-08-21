from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field must be set")
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(phone_number, password, **extra_fields)
    
class User(models.Model):
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.password

class Group(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_of')
    chair = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chair_of')
    signatories = models.ManyToManyField(User, related_name='signatories')

    def __str__(self):
        return self.admin
    
class UserRegistation(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'

    groups = models.ManyToManyField(Group, blank=True, related_name='user_registrations')
    user_permissions = models.ManyToManyField('auth.Permission', blank=True, related_name='user_registrations', related_query_name='user_registration_permission')


class CreateGroup(models.Model):
    GROUP_TYPES = [
        ('savings', 'Savings Group'),
        ('loan', 'Loan Group'),
    ]
    
    GROUP_ROLES = [
        ('admin', 'Admin'),
        ('member', 'Member'),
    ]
    
    CURRENCIES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('KES', 'Kenyan Shilling'),
        
    ]

    group_name = models.CharField(max_length=100)
    number_of_members = models.PositiveIntegerField()
    group_type = models.CharField(max_length=20, choices=GROUP_TYPES)
    group_role = models.CharField(max_length=20, choices=GROUP_ROLES)
    country_of_operation = models.CharField(max_length=50)
    group_currency = models.CharField(max_length=3, choices=CURRENCIES)

    def __str__(self):
        return self.group_name

class Contribution(models.Model):
    member_name=models.CharField(max_length=50)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fine_details=models.CharField(max_length=250)
    

    def __str__(self):
        return self.amount


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    repayment_months = models.PositiveIntegerField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.amount


class LoanFunding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount_funded = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.amount_funded


class Interest(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.date


class Fee(models.Model):
    short_name = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.description


class LoanExpenditure(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    budgeted_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2)
    last_spent_date = models.DateField()

    def __str__(self):
        return self.amount_spent


