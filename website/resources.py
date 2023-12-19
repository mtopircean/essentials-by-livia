from import_export import resources
from .models import AddProduct, AddPromotion, AppUser, Ailment


# AddProductResource: Defines a resource for handling import and export actions
# for the AddProduct model. It extends ModelResource from django-import-export.
class AddProductResource(resources.ModelResource):
    class Meta:
        model = AddProduct


# AddPromotionResource: Defines a resource for 
# handling import and export actions
# for the AddPromotion model. 
# It extends ModelResource from django-import-export.
class AddPromotionResource(resources.ModelResource):
    class Meta:
        model = AddPromotion


# AppUserResource: Defines a resource for handling import and export actions
# for the AppUser model. It extends ModelResource from django-import-export.
class AppUserResource(resources.ModelResource):
    class Meta:
        model = AppUser


# AddAilmentResource: Defines a resource for handling import and export actions
# for the Ailment model. It extends ModelResource from django-import-export.
class AddAilmentResource(resources.ModelResource):
    class Meta:
        model = Ailment
