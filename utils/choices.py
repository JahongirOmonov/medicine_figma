from django.db import models


class BloodGroup(models.TextChoices):
    A = 'A'
    B = 'B'
    AB = 'AB'
    O = 'O'
    DOB = 'DOB'
    AB_plus = 'AB+'


class PaymentMethod(models.TextChoices):
    DEBIT = 'Debit/Credit Card'
    NET_BANKING = 'Net Banking'
    PAYTM_WALLET = 'Paytm Wallet'
    UPI = 'Upi'
    GOOGLE_PAY = 'Google Pay'
    AMAZON_PAY = 'Amazon Pay'
    PHONE_PE = 'Phone Pe'
    LAZY_PAY = 'Lazy Pay'
    OLAMONEY = 'OlaMoney'
