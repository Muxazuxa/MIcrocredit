from django.forms import *
from .models import *


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CreditCreateForm(ModelForm):
    PERIOD = (
        ('Ежедневно', 'Ежедневно'),
        ('Еженедельно', 'Еженедельно'),
        ('Ежемесячно', 'Ежемесячно'),
    )
    customer_fio = CharField(max_length=100)
    customer_inn = CharField(max_length=100)
    user_username = CharField(max_length=100)
    period_type = ChoiceField(choices=PERIOD)

    class Meta:
        model = Credit
        fields = '__all__'
