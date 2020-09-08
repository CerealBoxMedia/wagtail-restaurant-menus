from wagtail.core.blocks import (
    CharBlock, StreamBlock, StructBlock, DecimalBlock, ChoiceBlock
)
from .menu_type_choices import MENU_TYPE_CHOICES


class ChefSpecialsItemStreamBlock(StructBlock):
    chef_special_item_name = CharBlock(required=True, blank=False)
    chef_special_item_description = CharBlock(required=True, blank=False)
    chef_special_item_price = DecimalBlock(required=True,
                                   blank=False,
                                   min_value=0.01,
                                   help_text="Item price in decimal format e.g. 19.50")

    class Meta:
        icon = "fa-star"
        template = "wagtailrestaurantmenus/chef_specials_block.html"


class MainsMenuItemStreamBlock(StructBlock):
    menu_item_name = CharBlock(required=True, blank=False)
    menu_item_description = CharBlock(required=True, blank=False)
    menu_item_price = DecimalBlock(required=True,
                                   blank=False,
                                   min_value=0.01,
                                   help_text="Item price in decimal format e.g. 12.50")

    class Meta:
        icon = "fa-cutlery"
        template = "wagtailrestaurantmenus/mains_menu_item_block.html"


class DessertsMenuItemStreamBlock(StructBlock):
    desserts_item_name = CharBlock(required=True, blank=False)
    desserts_item_description = CharBlock(required=True, blank=False)
    desserts_item_price = DecimalBlock(required=True,
                                   blank=False,
                                   min_value=0.01,
                                   help_text="Item price in decimal format e.g. 7.50")

    class Meta:
        icon = "fa-spoon"
        template = "wagtailrestaurantmenus/desserts_menu_item_block.html"


class SakeMenuItemStreamBlock(StructBlock):
    sake_item_name = CharBlock(required=True, blank=False)
    sake_item_description = CharBlock(required=False)
    sake_item_price = DecimalBlock(required=True,
                                   blank=False,
                                   min_value=0.01)

    class Meta:
        icon = "fa-jpy"
        template = "wagtailrestaurantmenus/beer_menu_item_block.html"


class WineMenuItemStreamBlock(StructBlock):
    wine_item_name = CharBlock(required=True, blank=False)
    wine_item_description = CharBlock(required=False)
    wine_item_price = DecimalBlock(required=True,
                                   blank=False,
                                   min_value=0.01)

    class Meta:
        icon = "fa-glass"
        template = "wagtailrestaurantmenus/wine_menu_item_block.html"


class BeerMenuItemStreamBlock(StructBlock):
    beer_item_name = CharBlock(required=True, blank=False)
    beer_item_description = CharBlock(required=False)
    beer_item_price = DecimalBlock(required=True,
                                     blank=False,
                                     min_value=0.01,)

    class Meta:
        icon = "fa-beer"
        template = "wagtailrestaurantmenus/beer_menu_item_block.html"


class HotDrinksMenuItemStreamBlock(StructBlock):
    hot_drinks_item_name = CharBlock(required=True, blank=False)
    hot_drinks_item_description = CharBlock(required=False)
    hot_drinks_item_price = DecimalBlock(required=True,
                                     blank=False,
                                     min_value=0.01)

    class Meta:
        icon = "fa-coffee"
        template = "wagtailrestaurantmenus/beer_menu_item_block.html"


class SodaMenuItemStreamBlock(StructBlock):
    soda_item_name = CharBlock(required=True, blank=False)
    soda_item_description = CharBlock(required=False)
    soda_item_price = DecimalBlock(required=True,
                                   blank=False,
                                   min_value=0.01)

    class Meta:
        icon = "fa-glass-whiskey"
        template = "wagtailrestaurantmenus/beer_menu_item_block.html"


class MenuTypeChoiceBlock(StructBlock):
    menu_item_choice = ChoiceBlock(choices=MENU_TYPE_CHOICES, blank=False, required=True)

    class Meta:
        icon='fa-signs'
        template = "wagtailrestaurantmenus/menu_type_block.html"


class BaseStreamBlock(StreamBlock):
    # This will pull the above into one streamfield instance as StreamPanel will only take one instance.
    mains_menu_item = MainsMenuItemStreamBlock()
    beer_menu_item = BeerMenuItemStreamBlock()
    wine_menu_item = WineMenuItemStreamBlock()
    sake_menu_item = SakeMenuItemStreamBlock()
    soda_menu_item = SodaMenuItemStreamBlock()
    hot_drinks_menu_item = HotDrinksMenuItemStreamBlock()
    desserts_menu_item = DessertsMenuItemStreamBlock()
    chefs_specials_item = ChefSpecialsItemStreamBlock()
    menu_type = MenuTypeChoiceBlock()