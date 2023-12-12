from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

import utils.customer_data
import utils.load_data

from .serializers import RegisterSerializer


class AddCustomerData(APIView):
    def post(self, request, *args, **kwargs):
        utils.customer_data.add_customer_data()
        return Response("Customer Data Added Successfully")


class AddLoanData(APIView):
    def post(self, request, *args, **kwargs):
        utils.load_data.add_loan_data()
        return Response("Loan Data Added Successfully")


class Register(generics.CreateAPIView):
    serializer_class = RegisterSerializer
