from django.shortcuts import render
from django.shortcuts import render
from Main.models import *

# Create your views here.

from datetime import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from Main.models import Group,CreateGroup,Contribution,LoanExpenditure,LoanFunding,Loan,Interest,Fee
from .serializers import (
Group,
CreateGroup,
Contribution,
LoanExpenditure,
LoanFunding,
Loan,
Interest,
Fee

   )

from drf_yasg.utils import swagger_auto_schema


from .serializers import *

from django.contrib.auth.hashers import make_password


# Create your views here.

# class UserRegistrationView(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = UserRegistrationSerializer

#     @swagger_auto_schema(responses={200: UserRegistrationSerializer(many=True)})
#     def get(self, format=None, *args, **kwargs):
#         user_registration= UserRegistration.objects.all()
#         serializer = UserRegistrationSerializer( user_registration, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     @swagger_auto_schema(request_body=UserRegistrationSerializer)
#     def post(self, request, format=None, *args, **kwargs):
#         serializers = UserRegistrationSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(data=serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        


# class UserLoginView(APIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = UserLoginSerializer

#     @swagger_auto_schema(responses={200: UserLoginSerializer(many=True)})
#     def get(self, format=None, *args, **kwargs):
#         user_login= UserLogin.objects.all()
#         serializer = UserLoginSerializer( user_login, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     @swagger_auto_schema(request_body=UserLoginSerializer)
#     def post(self, request, format=None, *args, **kwargs):
#         serializers = UserLoginSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(data=serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        


class GroupView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = GroupSerializer

    @swagger_auto_schema(responses={200: GroupSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        group= Group.objects.all()
        serializer = GroupSerializer( group, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=GroupSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = GroupSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CreateGroupView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateGroupSerializer

    @swagger_auto_schema(responses={200: CreateGroupSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        create_group= CreateGroup.objects.all()
        serializer = CreateGroupSerializer(create_group, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CreateGroupSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = CreateGroupSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ContributionView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContributionSerializer

    @swagger_auto_schema(responses={200: ContributionSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        contribution= Contribution.objects.all()
        serializer = ContributionSerializer(contribution, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ContributionSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = ContributionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoanExpenditureView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanExpenditureSerializer

    @swagger_auto_schema(responses={200: LoanExpenditureSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        loan_expenditure= LoanExpenditure.objects.all()
        serializer = LoanExpenditureSerializer(loan_expenditure, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LoanExpenditureSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LoanExpenditureSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoanFundingView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanFundingSerializer

    @swagger_auto_schema(responses={200: LoanFundingSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        loan_funding= LoanFunding.objects.all()
        serializer = LoanFundingSerializer(loan_funding, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LoanFundingSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LoanFundingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoanSerializer

    @swagger_auto_schema(responses={200: LoanSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        loan= Loan.objects.all()
        serializer = LoanSerializer(loan, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LoanSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LoanSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class InterestView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InterestSerializer

    @swagger_auto_schema(responses={200: InterestSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        interest= Interest.objects.all()
        serializer = InterestSerializer(interest, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=InterestSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = InterestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class FeeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = FeeSerializer

    @swagger_auto_schema(responses={200: FeeSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        fee= Fee.objects.all()
        serializer = FeeSerializer(fee, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=FeeSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = FeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

