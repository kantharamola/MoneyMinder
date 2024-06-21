from django.shortcuts import render, redirect
from .models import Budget, Expense, Wishlist, Remainder
from decimal import Decimal

def home(request):
    if request.method == 'POST':
        if 'budget' in request.POST:
            budget_amount = request.POST.get('budget')
            Budget.objects.all().delete()  # Clear the existing budget
            Budget.objects.create(amount=Decimal(budget_amount))

        elif 'expense_description' in request.POST and 'expense_amount' in request.POST:
            expense_description = request.POST.get('expense_description')
            expense_amount = request.POST.get('expense_amount')

            budget = Budget.objects.first()
            if budget is not None:
                try:
                    expense_amount = Decimal(expense_amount)

                    if expense_amount <= budget.amount:
                        budget.amount -= expense_amount
                        budget.save()
                        Expense.objects.create(description=expense_description, amount=expense_amount)
                    else:
                        return redirect('home')  # Redirect back to the form if expense exceeds budget

                except ValueError:
                    pass  # Handle the case where expense_amount is not a valid decimal

        elif 'wishlist_description' in request.POST and 'wishlist_amount' in request.POST:
            wishlist_description = request.POST.get('wishlist_description')
            wishlist_amount = request.POST.get('wishlist_amount')
            try:
                Wishlist.objects.create(description=wishlist_description, amount=Decimal(wishlist_amount))
            except ValueError:
                pass  # Handle the case where wishlist_amount is not a valid decimal

        elif 'remainder_description' in request.POST and 'remainder_date' in request.POST:
            remainder_description = request.POST.get('remainder_description')
            remainder_date = request.POST.get('remainder_date')
            Remainder.objects.create(description=remainder_description, due_date=remainder_date)

    budget = Budget.objects.first()
    expenses = Expense.objects.all()
    wishlists = Wishlist.objects.all()
    remainders = Remainder.objects.all()

    remaining_budget = Decimal('0.00')
    remaining_wishlist = Decimal('0.00')
    if budget is not None:
        remaining_budget = budget.amount - sum(expense.amount for expense in expenses)
        remaining_wishlist = budget.amount - sum(wishlist.amount for wishlist in wishlists)

    context = {
        'budget': budget,
        'expenses': expenses,
        'wishlists': wishlists,
        'remainders': remainders,
        'remaining_budget': remaining_budget,
        'remaining_wishlist': remaining_wishlist,
    }
    return render(request, 'home.html', context)
