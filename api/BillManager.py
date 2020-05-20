from .models import Customer
from .models import Bill


#
# class BillManager:
def get_bill_dict(bill):
    # {
    #     "billerBillID": "12123131322",
    #     "generatedOn": "2019-08-01T08:28:12Z",
    #     "recurrence": "ONE_TIME",
    #     "amountExactness": "EXACT",
    #     "customerAccount": {
    #         "id": "8208021440"
    #     },
    #     "aggregates": {
    #         "total": {
    #             "displayName": "Total Outstanding",
    #             "amount": {
    #                 "value": 99000
    #             }
    #         }
    #     }
    # }
    bill_dict = {}
    bill_dict["billerBillID"] = bill.id
    bill_dict["generatedOn"] = bill.created_at
    # bill["recurrence"] =
    bill_dict["customerAccount"] = {"id": bill.cust_id}
    bill_dict["aggregates"]={"total": {"displayName": "Total Outstanding", "amount": {"value" : bill.amount}}}
    return bill_dict


def fetch_bills_of_user(cust_phone):
    customer = Customer.objects.filter(phone=cust_phone).first()

    result = None

    # scene 1 - customer does not exists
    if customer is None:
        return {
            "status": 404,
            "success": False,
            "error": {
                "code": "customer-not-found",
                "title": "Customer not found",
                "detail": "The requested customer was not found in the biller system.",
                "traceID": "",
                "docURL": ""
            }
        }
    bills = Bill.objects.filter(cust_id=customer.id, status="UNPAID")

    # scene 2 - customer exists but no unpaid bills
    if customer is not None and len(bills) == 0:
        return {
            "status": 200,
            "success": True,
            "data": {
                "customer": {
                    "name": customer.name
                },
                "billDetails": {
                    "billFetchStatus": bills.status,
                    "bills": []
                }
            }
        }

    # scene 3 - customer exists and has unpaid bills
    if Customer is not None and len(bills) > 0:
        bill_list = []
        for bill in bills:
            bill_dict = get_bill_dict(bill)
            bill_list.append(bill_dict)
        return {
            "status": 200,
            "success": True,
            "data": {
                "customer": {
                    "name": "Ashok Kumar"
                },
                "billDetails": {
                    "billFetchStatus": "AVAILABLE",
                    "bills": bill_list
                }
            }
        }

    return result


def does_customer_exists(self, cust_phone):
    return Customer.objects.filter(phone=cust_phone).exists()


def does_customer_has_outstanding_bills(self, cust_id):
    return Bill.objects.filter(cust_id=cust_id, status="UNPAID").exists()
