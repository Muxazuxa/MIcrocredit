from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Credit)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('get_fio', 'address', 'job_place', 'get_summ_leave', 'contacts')

    def get_fio(self, obj):
        return obj.credit.customer.fio

    def get_summ_leave(self, obj):
        return obj.credit.summ_leave


@admin.register(Graphic)
class GraphicAdmin(admin.ModelAdmin):
    list_display = ('summ_cut', 'summ_after_cut', 'date', 'user')