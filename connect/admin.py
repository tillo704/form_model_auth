from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Contact)
# admin.site.register(Product)
# admin.site.register(Category)



class ProductInline(admin.StackedInline):
    model = Product
    extra = 1
@admin.register(Category)
class CatgotyAdmin(admin.ModelAdmin):
    list_display  =  ('title','slug')
    search_fields = ('title',)
    inlines = [ProductInline]
    prepopulated_fields= {'slug':('title',)}