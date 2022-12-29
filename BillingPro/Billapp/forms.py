from django import forms
from Billapp.models import Billing,EstimatedBill, CombinedBilling


class BillingForm(forms.ModelForm):
    class Meta:
        model= Billing
        fields='__all__'

class EstimatedBillForm(forms.ModelForm):
    class Meta:
        model= EstimatedBill
        fields='__all__'

class CombinedBillingForm(forms.ModelForm):
    class Meta:
        model= CombinedBilling
        fields='__all__'
