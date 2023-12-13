from django.urls import path

from .views import AddCustomerData, AddLoanData, CheckLoanEligibity, Register

urlpatterns = [
    path("register", Register.as_view()),
    path("add_customer_data", AddCustomerData.as_view()),
    path("add_loan_data", AddLoanData.as_view()),
    path("check-eligibility", CheckLoanEligibity.as_view()),
]
