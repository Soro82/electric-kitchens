from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Wishlist
from products.models import Product
from profiles.models import UserProfile


@login_required
def wishlist(request):
    """
    A view to display a user's Wishlist.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user=profile)

    return render(
        request, 'wishlist/wishlist.html', {'wishlist': wishlist}
    )
