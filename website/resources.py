from import_export import resources
from .models import AddProduct, AddPromotion, AppUser, Ailment


class AddProductResource(resources.ModelResource):
    class Meta:
        model = AddProduct


class AddPromotionResource(resources.ModelResource):
    class Meta:
        model = AddPromotion


class AppUserResource(resources.ModelResource):
    class Meta:
        model = AppUser
        
class AddAilmentResource(resources.ModelResource):
    class Meta:
        model = Ailment