from .models import Customer, Loan


def create_customer(
    first_name: str,
    last_name: str,
    age: int,
    monthly_salary: int,
    phone_number: str,
    approved_limit,
) -> Customer:
    customer = Customer.objects.create(
        first_name=first_name,
        last_name=last_name,
        age=age,
        monthly_salary=monthly_salary,
        phone_number=phone_number,
        approved_limit=approved_limit,
    )
    return customer
