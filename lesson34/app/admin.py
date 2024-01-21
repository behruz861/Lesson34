from django.contrib import admin

from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(BuyHistory)
admin.site.register(Comment)
admin.site.register(Like)
