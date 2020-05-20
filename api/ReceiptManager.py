import datetime

from api.models import Bill, Receipt


def create_recipt(bill_id, platform_txn_ref_id):
    receipt = Receipt.objects.create(bill_id=bill_id, platform_txn_ref_id=platform_txn_ref_id, created_at=datetime.datetime.utcnow())
    return receipt


def update_ledger(bill, amount_paid=0):
    Bill.objects.filter(id=bill.id).update(remaining_amount=(bill.amount - amount_paid))
    return None
