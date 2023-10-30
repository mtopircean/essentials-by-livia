from django.contrib import admin
from .models import Ailment
from .models import AddProduct
from .models import AddPromotion

admin.site.register(Ailment)
admin.site.register(AddProduct)
admin.site.register(AddPromotion)