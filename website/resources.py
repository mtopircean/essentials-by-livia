from import_export import resources
from .models import AddProduct, AddPromotion, AppUser, Ailment


class AddProductResource(resources.ModelResource):
    """
    AddProductResource: Defines a resource for handling
    import and export actionsfor the AddProduct model.
    It extends ModelResource from django-import-export.
    """
    class Meta:
        model = AddProduct


class AddPromotionResource(resources.ModelResource):
    """
    AddPromotionResource: Defines a resource for
    handling import and export actions
    for the AddPromotion model.
    It extends ModelResource from django-import-export.
    """
    class Meta:
        model = AddPromotion


class AppUserResource(resources.ModelResource):
    """
    AppUserResource: Defines a resource for handling import and export actions
    for the AppUser model. It extends ModelResource from django-import-export.
    """
    class Meta:
        model = AppUser


class AddAilmentResource(resources.ModelResource):
    """
    AddAilmentResource: Defines a resource for handling
    import and export actions for the Ailment model.
    It extends ModelResource from django-import-export.
    """
    class Meta:
        model = Ailment
