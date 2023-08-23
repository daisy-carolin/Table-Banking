from django.urls import path
from . import views
#create your urls here
#api urls   
urlpatterns = [
# path('user_regstration', views.UserRegistrationView.as_view(),name='user_regstration_api'),
# path('user_login', views.UserLoginView.as_view(),name='user_login_api'),
path('group',views.GroupView.as_view(),name='group_api'),
path('create_group',views.CreateGroupView.as_view(),name='create_group_api'),
path('contribution',views.ContributionView.as_view(),name='contribution_api'),
path('loan_expenditure',views.LoanExpenditureView.as_view(),name='loan_expenditure_api'),
path('laon_funding',views.LoanFundingView.as_view(),name='laon_funding_api'),
path('loan',views.LoanView.as_view(),name='loan__api'),
path('interest',views.LoanFundingView.as_view(),name='interest_api'),
path('fee',views.FeeView.as_view(),name='fee_api'),

]