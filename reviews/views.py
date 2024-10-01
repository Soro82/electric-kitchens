from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from products.models import Product
from profiles.models import UserProfile


@login_required
def reviews(request):
    """ A view to show user reviews."""
