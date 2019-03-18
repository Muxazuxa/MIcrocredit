from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Customer(models.Model):
    fio = models.CharField(blank=False, max_length=100, verbose_name='Ф.И.О.')
    inn = models.CharField(blank=True, max_length=30, verbose_name='INN')
    passport = models.CharField(blank=True, max_length=50, verbose_name='Паспорт')
    address = models.CharField(blank=True, max_length=100, verbose_name='Адрес')
    job_place = models.CharField(blank=True, max_length=100, verbose_name='Место Бизнеса')
    contacts = models.CharField(blank=True, max_length=100, verbose_name='Контакты')

    def __str__(self):
        return str(self.fio)

    def get_absolute_url(self):
        return reverse('credit:customer_list')

    class Meta:
        unique_together = ['inn', 'passport']
        verbose_name='Заемщик'
        verbose_name_plural='Заемщики'


class Credit(models.Model):
    PERIOD = (
        ('Ежедневно', 'Ежедневно'),
        ('Еженедельно', 'Еженедельно'),
        ('Ежемесячно', 'Ежемесячно'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Ф.И.О.')
    filial = models.CharField(blank=False, max_length=50, verbose_name='Филиал')
    pay_count = models.IntegerField(blank=False, verbose_name='Количество платежей')
    period_type = models.CharField(blank=False, choices=PERIOD, max_length=20, verbose_name='Периодичнось выплат')
    percent = models.IntegerField(blank=False, verbose_name='Процент')
    summ = models.DecimalField(blank=False, decimal_places=2, max_digits=10, verbose_name='Сумма выдачи')
    summ_leave = models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Остаток')
    data_get = models.DateField(blank=False, verbose_name='Дата получения')
    data_close = models.DateField(blank=False, verbose_name='Дата погашения')
    summ_return = models.DecimalField(blank=False, decimal_places=2, max_digits=10, verbose_name='Сумма возврата')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Исполнитель')

    def __str__(self):
        return str(self.customer)

    def get_absolute_url(self):
        return reverse('credit:customer_list')

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


class Graphic(models.Model):
    credit = models.ForeignKey(Credit, on_delete=models.CASCADE)
    summ_cut = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма погашения')
    date = models.DateField(auto_now_add=True, verbose_name='Дата погашения')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Исполнитель')

    def __str__(self):
        return self.credit

    def get_absolute_url(self):
        return reverse('credit:credit_list')

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'График'










