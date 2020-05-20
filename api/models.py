from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6789]\d{9}$',
    message="Phone number must be entered in the format: \"+917760601643\". Up to 13 digits allowed."
)


class Customer(models.Model):
    name = models.CharField(max_length=1024, null=False)
    phone = models.CharField(max_length=17, blank=False, null=False)


class Bill(models.Model):
    cust_id = models.IntegerField(null=False)
    amount = models.BigIntegerField(null=False, default=0)
    status = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(null=False, default=0)
    current_active = models.BooleanField(default=True)
    remaining_amount = models.BigIntegerField(null=False, default=0)


class Receipt(models.Model):
    bill_id = models.IntegerField(null=False)
    status = models.CharField(max_length=255, blank=False, null=False)
    amount = models.BigIntegerField(null=False, default=0)
    payment_ref_id = models.CharField(max_length=255, blank=False, null=False)
    platform_txn_ref_id = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(null=False, default=0)
