from django import forms


class ProductForm(forms.Form):
    """ProductForm definition."""
    name = forms.CharField(max_length=20)
    quantity = forms.IntegerField()
