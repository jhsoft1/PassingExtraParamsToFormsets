from django import forms
from django.forms import BaseFormSet, formset_factory

from accounts.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ["description"]


def get_account_choices(user):
    return {1, 2, 3}


class TransactionBaseFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(TransactionBaseFormSet, self).__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        form = super(TransactionBaseFormSet, self)._construct_form(i, **kwargs)
        account_choices = get_account_choices(self.user)
        form.fields["account_debit"].choices = account_choices
        form.fields["account_credit"].choices = account_choices
        form.fields["DELETE"].label = "Duplicate"
        return form


TransactionFormSet = formset_factory(TransactionForm, can_delete=True, extra=0,
                                     formset=TransactionBaseFormSet)
