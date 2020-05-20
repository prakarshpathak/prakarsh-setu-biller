import datetime
import json
from enum import Enum

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from django.http import HttpResponseForbidden

from api import ReceiptManager
from . import BillManager
from .Authenticator import Authenticator
# Create your views here.
from .BillManager import fetch_bills_of_user
from .ReceiptManager import update_ledger, create_recipt
from .models import Customer, Bill


class CustomerAttribute(Enum):
    MobileNum = "mobileNumber"


def create_customer():
    Customer.objects.create(name="TesNAmr", phone="123456889")
    Bill.objects.create(cust_id=1, amount=900056, status="UNPAID", created_at=datetime.datetime.utcnow(),
                        current_active=True)
    # customer1.save()


class BillView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bill_manager = BillManager
        self.authenticator = Authenticator()

    def get(self, request):
        bearer_token = request.headers.get('Authorization', '')
        if len(bearer_token) < 1 or self.authenticator.authenticated(bearer_token[7:]):
            return HttpResponseForbidden()
        # get bills of user from request.POST.get(..)'
        # result = self.bill_manager.BillManager.fetch_bills_of_user(request.POST.get(....))
        data = request.body
        request_body = json.loads(data)
        # bill_manager = BillManager()
        customer_identifiers = request_body['customerIdentifiers']
        # create_customer()
        for customer in customer_identifiers:
            if customer['attributeName'] == CustomerAttribute.MobileNum.value:
                response = fetch_bills_of_user(customer["attributeValue"])

        # response ={
        #     "status": 404,
        #     "success": False,
        #     "error": {
        #         "code": "customer-not-found",
        #         "title": "Customer not found",
        #         "detail": "The requested customer was not found in the biller system.",
        #         "traceID": "",
        #         "docURL": ""
        #     }
        # }
        return JsonResponse(response)


class ReceiptView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reciept_manager = ReceiptManager
        self.authenticator = Authenticator()

    def get(self, request):
        bearer_token = request.headers.get('Authorization', '')
        # authenticator = Authenticator()
        if len(bearer_token) < 1 or self.authenticator.authenticated(token=bearer_token[7:]):
            return HttpResponseForbidden()

        # {
        #     "billerBillID": "12123131322",
        #     "platformBillID": "SETU121341312121",
        #     "paymentDetails": {
        #         "platformTransactionRefID": "TXN12121219",
        #         "uniquePaymentRefID": "XXXXAYYDDD999999",
        #         "amountPaid": {
        #             "value": 99000
        #         },
        #         "billAmount": {
        #             "value": 99000
        #         }
        #     }
        # }
        data = request.body
        request_body = json.loads(data)
        bill_id = request_body["billerBillID"]
        platform_build_id = request_body["platformBillID"]
        payment_details = request_body["paymentDetails"]
        payment_ref_id = payment_details["platformTransactionRefID"]
        amount_paid = payment_details["amountPaid"]["value"]
        bill = Bill.objects.filter(id=bill_id)[0]
        receipt = create_recipt(bill_id, payment_ref_id)
        update_ledger(bill, amount_paid=amount_paid)

        response = {
            "status": 200,
            "success": True,
            "data": {
                "billerBillID": bill_id,
                "platformBillID": platform_build_id,
                "platformTransactionRefID": payment_ref_id,
                "receipt": {
                    "id": receipt.id,
                    "date": receipt.created_at
                }
            }
        }
        return JsonResponse(response)
