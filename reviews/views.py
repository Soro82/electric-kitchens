from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from products.models import Product
from profiles.models import UserProfile


@login_required
def see_reviews(request):
    """ A view to show user reviews."""
    reviews = Review.objects.filter(author=request.user)

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Displays the form for logged in users to add a review. """
    product = get_object_or_404(Product, pk=product_id)

    user_review = Review.objects.filter(
        author=request.user, product=product)

    if user_review:
        messages.error(request,
                       'You have already submitted a review for this product')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.instance.product = product
                form.save()
                messages.success(request,
                                 'Your product review has been submitted')

                update_ratings(product)

                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to submit the review. \
                    Please ensure the form is valid.')
        else:
            form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def update_ratings(product):
    """
    Update a product's ratings with the rating given by
    the user in each review.
    """
    all_reviews = Review.objects.filter(product=product)
    num_reviews = all_reviews.count()
    total_rating = 0
    total_ease_of_use = 0
    total_energy_efficiency = 0

    if num_reviews <= 0:
        product.rating = None
    else:
        for review in all_reviews:
            total_rating += review.rating
            total_ease_of_use += review.ease_of_use
            total_energy_efficiency += review.energy_efficency

        product.rating = total_rating / num_reviews
        product.ease_of_use = total_ease_of_use / num_reviews
        product.energy_efficency = total_energy_efficiency / num_reviews

    product.save()
