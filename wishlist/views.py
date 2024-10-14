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


@login_required
def add_to_wishlist(request, product_id):
    """ Add a product to the user's Wishlist. """
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)

    # Check if the product is already in the users wishlist
    if Wishlist.objects.filter(
        user=user,
        product=product
    ).exists():
        messages.warning(
            request, f'{product.name} is already in your Wishlist.')
    else:
        # create a new wishlist
        wishlist = Wishlist.objects.create(
            user=user, product=product)
        messages.success(
            request,
            f'{wishlist.product.name} added to Wishlist successfully!'
        )

    # Redirect to the product detail page
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove a product from the user's Wishlist. """
    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)

    wishlist_product = Wishlist.objects.get(user=user,
                                            product=product)
    wishlist_product.delete()
    messages.success(request, f'{product.name} has been successfully removed.')
    return redirect(reverse('wishlist'))
