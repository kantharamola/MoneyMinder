from django import forms
from .models import Expense, Wishlist

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['description', 'amount']
