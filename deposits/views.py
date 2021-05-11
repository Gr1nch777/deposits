from django.shortcuts import render
from django.views.generic import ListView, View, FormView, DetailView
from deposits.models import Deposit
from deposits.forms import DepositForm


class DepositListView(ListView):

    model = Deposit
    template_name = 'all_deposits.html'


class DepositDetailView(DetailView):
    model = Deposit
    template_name = 'deposit.html'


class AddDepositView(FormView):

    form_class = DepositForm
    template_name = 'add_deposit.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response
