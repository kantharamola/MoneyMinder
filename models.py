from django.db import models

class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Budget: {self.amount}'

from django.utils.timezone import now

class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.description


class Wishlist(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.description

class Remainder(models.Model):
    description = models.CharField(max_length=200)
    due_date = models.DateField()

    def __str__(self):
        return self.description
