from django.urls import path

from .views import AddCustomerData, Register

urlpatterns = [
    path("register", Register.as_view()),
    path("add_customer_data", AddCustomerData.as_view()),
]
