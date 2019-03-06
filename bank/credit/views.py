from django.shortcuts import render
from . models import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CustomerListView(LoginRequiredMixin, ListView):
    context_object_name = 'customers'
    template_name = 'credit/customer_list.html'

    def get_queryset(self):
        return Customer.objects.all()
