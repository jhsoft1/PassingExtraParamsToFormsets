from django.db import models
from django.db.models import DO_NOTHING


# https://reinbach.com/posts/django-formsets-with-extra-params/

class Account(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f'{self.number}'


class Transaction(models.Model):
    account_debit = models.ForeignKey(Account, related_name="debit",
                                      verbose_name="debit", on_delete=DO_NOTHING)
    account_credit = models.ForeignKey(Account, related_name="credit",
                                       verbose_name="credit", on_delete=DO_NOTHING)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    summary = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.account_debit} {self.account_credit} {self.amount} {self.summary}'
