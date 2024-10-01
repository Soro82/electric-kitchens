from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Review(models.Model):
    """ A model to store user's review information. """
    RATING_OPTIONS = ((0, "1 - Very Unsatisfied"), (1, "2 - Unsatisfied"),
                      (2, "3 - Satisfied"), (3, "4 - Very Satisfied"),
                      (4, "5 - Extremely Satisfied"))
    
    EASE_OF_USE_OPTIONS = ((0, "1 - Very Hard"), (1, "2 - Hard"),
                      (2, "3 - Not Easy or Hard"), (3, "4 - Easy"),
                      (4, "5 - Very Easy"))
    
    ENEGERY_OPTIONS = ((0, "1 - Very Inefficient"), (1, "2 - Inefficient"),
                      (2, "3 - Neither"), (3, "4 - Efficient"),
                      (4, "5 - Very Efficient"))

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='review_author')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_OPTIONS, default=2)
    ease_of_use = models.IntegerField(choices=EASE_OF_USE_OPTIONS, default=2)
    energy_efficency = models.IntegerField(choices=ENEGERY_OPTIONS, default=2)
    purchase_date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.product} review by {self.author}'
