from django.contrib import admin
from models import Resturant, Food, Comment
# Register your models here.

class ResturantAdmin(admin.ModelAdmin):
	list_display = ('name', 'phonenumber', )

class FoodAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'is_spicy', 'comment', 'resturant', )
	list_filter = ('is_spicy', )

admin.site.register(Resturant, ResturantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment)