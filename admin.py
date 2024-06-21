from django.contrib import admin
from .models import Budget, Expense, Wishlist, Remainder

admin.site.register(Budget)
admin.site.register(Expense)
admin.site.register(Wishlist)
admin.site.register(Remainder)
