from . forms import *
# from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.


class CustomerListView(LoginRequiredMixin, ListView):
    context_object_name = 'customers'
    template_name = 'credit/customer_list.html'

    def get_queryset(self):
        return Customer.objects.all()


class CustomerCreateView(LoginRequiredMixin, CreateView):
    form_class = CustomerCreateForm
    template_name = 'credit/customer_add.html'


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'credit/customer_update.html'


class CreditCreateView(LoginRequiredMixin, CreateView):
    form_class = CreditCreateForm
    template_name = 'credit/credit_add.html'

    def get_form(self):
        form = super(CreditCreateView, self).get_form()
        initial_base = self.get_initial()
        customer = Customer.objects.get(pk=self.kwargs['pk'])
        initial_base['customer'] = customer
        initial_base['customer_fio'] = customer.fio
        initial_base['customer_inn'] = customer.inn
        user = self.request.user
        initial_base['user'] = user
        initial_base['user_username'] = user.username
        form.initial = initial_base
        return form


class CreditListView(LoginRequiredMixin, ListView):
    context_object_name = 'credits'
    template_name = 'credit/credit_list.html'

    def get_queryset(self):
        return Credit.objects.all()






