from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login_user/', views.login_user, name='login'),
    path('', views.home, name='dashboard'),
    path('join_group/', views.join_group, name='join_group'),
    path('create_group/', views.create_group, name='create_group'),
    path('group_set_up/', views.group_set_up, name='group_set_up'),
    path('add_member/', views.add_member, name='add_member'),
    path('member_contribution/', views.member_contribution, name='member_contribution'),
    path('contribute/<int:contribution_id>/', views.contribute, name='contribute'),
    path('request_loan/', views.request_loan, name='request_loan'),
    path('fund_loan/<int:loan_id>/', views.fund_loan, name='fund_loan'),
    path('loan_expenditure/<int:loan_id>/', views.loan_expenditure, name='loan_expenditure'),
    path('borrow/', views.borrow_loan, name='borrow_loan'),
    path('fund/<int:loan_id>/', views.fund_loan, name='fund_loan'),
    path('repay/<int:loan_id>/', views.repay_loan, name='repay_loan'),

]