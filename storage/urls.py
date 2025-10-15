from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from storage.views import CartridgeRefreshListView, CartridgePrintListView, CartridgePrintListFileView, CartridgePrintBarcodeView, CartridgeListView, StorageHomeView, SnapshotHomeView, SnapshotDetailView, SnapshotAddView

app_name = 'storage'

urlpatterns = [
    path('', StorageHomeView.as_view(), name='index'),
    path('cartridges/refresh/', CartridgeRefreshListView.as_view(), name='cartridge_refresh'),
    path('cartridges/print_list/', CartridgePrintListView.as_view(), name='print_list'),
    path('cartridges/print_list_file/', CartridgePrintListFileView.as_view(), name='print_list_file'),
    path('cartridges/print_barcode/', CartridgePrintBarcodeView.as_view(), name='print_barcode'),    
    path('cartridges/', CartridgeListView.as_view(), name='cartridge_list'),
    path('snapshot/<int:pk>/', SnapshotDetailView.as_view(), name='snapshot_detail'),
    path('snapshots/add/', SnapshotAddView.as_view(), name='snapshots_add'),
    path('snapshots/', SnapshotHomeView.as_view(), name='snapshots'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)