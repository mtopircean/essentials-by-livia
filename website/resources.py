from import_export import resources
from .models import AddProduct, AddPromotion, AppUser


class AddProductResource(resources.ModelResource):
    class Meta:
        model = AddProduct


class AddPromotionResource(resources.ModelResource):
    class Meta:
        model = AddPromotion


class AppUserResource(resources.ModelResource):
    class Meta:
        model = AppUser