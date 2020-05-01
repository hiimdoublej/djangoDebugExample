from django.contrib import admin

from shop_app.models import Owner, Shop, Item


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'owned_items')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.prefetch_related('shop_set__item_set')
        return qs

    def owned_items(self, obj):
        items = []
        for shop in obj.shop_set.all():
            items.extend(shop.item_set.all())
        if len(items) > 0:
            return ','.join(x.name for x in items)
        return '-'


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'owner')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'shop')
