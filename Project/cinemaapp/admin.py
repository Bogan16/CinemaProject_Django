# from django.contrib import admin
# from .models import Movie, Ticket, Customer, Places

# admin.site.register(Movie)
# admin.site.register(Ticket)
# admin.site.register(Customer)
# admin.site.register(Places)

from django import forms
from django.contrib import admin
from .models import Movie, Ticket, Customer, Places

class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    tickets = forms.ModelMultipleChoiceField(
        queryset=Ticket.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm

admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Places)



