from rest_framework import serializers

from .crud import (create_customer, create_loan_with_customer_id,
                   get_correct_interest_rate, get_credit_rating,
                   get_customer_from_customer_id, get_monthly_installment)
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


class CreateLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["customer_id", "loan_amount", "tenure", "interest_rate"]

    def create(self, data):
        customer = get_customer_from_customer_id(
            customer_id=data["customer_id"].customer_id
        )
        credit_rating = get_credit_rating(
            customer=customer,
            customer_id=data["customer_id"],
            loan_amount=data["loan_amount"],
            approved_limit=customer.approved_limit,
        )

        correct_interest_rate = get_correct_interest_rate(
            credit_rating=credit_rating, interest_rate=data["interest_rate"]
        )
        monthly_installment = get_monthly_installment(
            interest_rate=correct_interest_rate,
            loan_amount=data["loan_amount"],
            tenure=data["tenure"],
        )
        loan_obj = create_loan_with_customer_id(
            customer_id=data["customer_id"],
            loan_amount=data["loan_amount"],
            tenure=data["tenure"],
            interest_rate=data["interest_rate"],
            monthly_emi=monthly_installment,
        )
        return loan_obj

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["loan_id"] = instance.loan_id
        data["loan_approved"] = True
        data["message"] = "Congratulations! You're loan is approved"
        data["monthly_installment"] = instance.monthly_emi
        data.pop("loan_amount")
        data.pop("tenure")
        data.pop("interest_rate")

        response_data = {"success": True, "data": data}

        return response_data
