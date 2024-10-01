from django import forms
from datetime import date
from .models import Review


class DateInput(forms.DateInput):
    """
    Allows the user to choose a date from a calender
    in the Review Form.
    """
    input_type = "date"


class ReviewForm(forms.ModelForm):
    """
    This class creates the form for users to add a review.
    """
    class Meta:
        model = Review
        fields = ('content', 'rating', 'ease_of_use', 'energy_efficency',
                  'purchase_date')
        widgets = {"purchase_date": DateInput()}
        labels = {
            'ease_of_use': 'Ease of Use',
            'energy_efficency': 'Energy Efficiency',
            'purchase_date': 'Date of Purchase',
        }
