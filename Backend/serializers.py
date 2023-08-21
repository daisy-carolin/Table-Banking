from rest_framework import serializers, fields
from Main.models import Group,CreateGroup,Contribution,LoanExpenditure,LoanFunding,Loan,Interest,Fee
from .models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')


class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateGroup
        fields = ('__all__')


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('__all__')


class LoanExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanExpenditure
        fields = ('__all__')


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('__all__')


class LoanExpendtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanExpenditure
        fields = ('__all__')


class LoanFundingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanFunding
        fields = ('__all__')


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('__all__')


class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = ('__all__')