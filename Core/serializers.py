from rest_framework import serializers

from .crud import create_customer
from .models import Customer, Loan


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "age", "monthly_salary", "phone_number"]

    @staticmethod
    def create(data):
        approved_limit = round(36 * data["monthly_salary"], -5)
        customer = create_customer(
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data["age"],
            monthly_salary=data["monthly_salary"],
            phone_number=data["phone_number"],
            approved_limit=approved_limit,
        )
        return customer

    @staticmethod
    def to_representation(instance):
        data = super().to_representation(instance)
        data["approved_limit"] = instance.approved_limit

        response_data = {"success": True, "data": data}

        return response_data
