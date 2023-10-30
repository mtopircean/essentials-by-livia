from django.contrib import admin
from .models import Ailment
from .models import AddProduct
from .models import AddPromotion
from django_summernote.admin import SummernoteModelAdmin

@admin.register(AddProduct)
class AddProductAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')


@admin.register(AddPromotion)
class AddPromotionAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')


admin.site.register(Ailment)