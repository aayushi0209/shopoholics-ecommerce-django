from django.contrib import admin
# from django.contrib.auth.models import Group
from .models import Product, Contact,Orders,OrderUpdate


admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)