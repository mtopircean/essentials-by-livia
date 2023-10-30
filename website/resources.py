from import_export import resources
from .models import AddProduct, AddPromotion


class AddProductResource(resources.ModelResource):
    class Meta:
        model = AddProduct


class AddPromotionResource(resources.ModelResource):
    class Meta:
        model = AddPromotion