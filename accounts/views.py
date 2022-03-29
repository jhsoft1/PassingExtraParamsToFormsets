from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import TransactionFormSet


class TransactionImportConfirmView(FormView):
    template_name = "import.html"
    form_class = TransactionFormSet
    success_url = reverse_lazy("list")

    def get_form_kwargs(self):
        kwargs = super(TransactionImportConfirmView, self).get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
