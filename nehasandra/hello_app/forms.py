from django import forms

from hello_app.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields='__all__'