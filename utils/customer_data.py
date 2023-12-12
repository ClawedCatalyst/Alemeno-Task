import pandas as pd

from Core.models import Customer


def add_customer_data():
    df = pd.read_excel("utils/customer_data.xlsx")
    for row in df.iterrows():
        phone_number = "+91" + str(row["Phone Number"])
        Customer.objects.create(
            customer_id=row["Customer ID"],
            first_name=row["First Name"],
            last_name=row["Last Name"],
            age=row["Age"],
            phone_number=phone_number,
            monthly_salary=row["Monthly Salary"],
            approved_limit=row["Approved Limit"],
        )
