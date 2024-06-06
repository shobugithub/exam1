from django import forms
from blog.models import Customers

class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['full_name','email', 'phone', 'billing_address','description', 'vat_number', 'invoice_prefix']