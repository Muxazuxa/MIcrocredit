from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cash)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fio', 'address', 'job_place', 'contacts')


@admin.register(Graphic)
class GraphicAdmin(admin.ModelAdmin):
    list_display = ('summ_cut', 'summ_after_cut', 'date', 'user')


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('get_fio', 'summ', 'summ_leave', 'summ_return', 'data_get', 'data_close', 'user', 'date' )

    def get_fio(self, obj):
        return obj.customer.fio