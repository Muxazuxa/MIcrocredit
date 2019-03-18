from django.forms import *
from .models import *


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CreditCreateForm(ModelForm):
    customer_fio = CharField(max_length=100)
    customer_inn = CharField(max_length=100)
    user_username = CharField(max_length=100)

    class Meta:
        model = Credit
        fields = '__all__'


class GraphicCreateForm(ModelForm):
    customer = CharField(max_length=100)
    summ_leave = CharField(max_length=100)
    user_username = CharField(max_length=100)

    class Meta:
        model = Graphic
        fields = '__all__'
