from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from storage.views import CartridgeRefreshView, CartridgeLoadPrintListView, CartridgeBarcodeListView, CartridgeListView, StorageHomeView, SnapshotHomeView, SnapshotDetailView, SnapshotAddView

app_name = 'storage'

urlpatterns = [
    path('', StorageHomeView.as_view(), name='index'),
    path('cartridges/refresh/', CartridgeRefreshView.as_view(), name='cartridge_refresh'),
    path('cartridges/load_print_list/', CartridgeLoadPrintListView.as_view(), name='load_print_list'),
    path('cartridges/barcode_list/', CartridgeBarcodeListView.as_view(), name='barcode_list'),
    path('cartridges/', CartridgeListView.as_view(), name='cartridge_list'),
    path('snapshot/<int:pk>/', SnapshotDetailView.as_view(), name='snapshot_detail'),
    path('snapshots/add/', SnapshotAddView.as_view(), name='snapshots_add'),
    path('snapshots/', SnapshotHomeView.as_view(), name='snapshots'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

