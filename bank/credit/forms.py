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
    summ_leave = DecimalField(decimal_places=2)
    summ_cut = DecimalField(decimal_places=2)
    user_username = CharField(max_length=100)

    def clean(self):
        cleaned_data = super(GraphicCreateForm, self).clean()
        summ_cut = cleaned_data.get('summ_cut')
        summ_leave = cleaned_data.get('summ_leave')
        if summ_cut > summ_leave:
            raise ValidationError({'summ_cut': ["Сумма погашения не может быть больше оставшейся суммы"]})
        return cleaned_data

    class Meta:
        model = Graphic
        fields = '__all__'



