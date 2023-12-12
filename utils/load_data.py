import pandas as pd

from Core.models import Customer, Loan


def add_loan_data():
    df = pd.read_excel("utils/loan_data.xlsx")
    for index, row in df.iterrows():
        customer_obj = Customer.objects.get(customer_id=row["Customer ID"])
        Loan.objects.update_or_create(
            customer_id=customer_obj,
            loan_id=row["Loan ID"],
            loan_amount=row["Loan Amount"],
            tenure=row["Tenure"],
            interest_rate=row["Interest Rate"],
            monthly_emi=row["Monthly payment"],
            emi_paid_on_time=row["EMIs paid on Time"],
            start_date=row["Date of Approval"],
            end_date=row["End Date"],
        )
