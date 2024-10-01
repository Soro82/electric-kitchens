from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'product',
        'rating',
        'ease_of_use',
        'energy_efficency',
        'purchase_date',
        'created_on',
    )

    ordering = ('author',)


admin.site.register(Review, ReviewAdmin)
