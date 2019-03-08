from django.forms import *
from .models import Customer


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'



