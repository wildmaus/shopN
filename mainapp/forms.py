from django import forms
from .models import Order
from datetime import date
from django.core.exceptions import ValidationError


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order_date'].label = 'Дата получения заказа'

    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    def clean_order_date(self):
        if self.cleaned_data['order_date']:
            if self.cleaned_data['order_date'] <= date.today():
                raise ValidationError('Выберете актуальную дату, не раньше завтра')
        return self.cleaned_data['order_date']

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'address', 'buying_type', 'order_date', 'comment'
        )


