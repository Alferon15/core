from django.contrib import admin
from storage.models import Cartridge, Snapshot, Item


@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['number', 'article', 'caption']
    list_display_links = ['number']


@admin.register(Snapshot)
class SnapshotAdmin(admin.ModelAdmin):
    list_display = ['dt']
    list_display_links = ['dt']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cartridge', 'snapshot']
    list_display_links = ['pk']
