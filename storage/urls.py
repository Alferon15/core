from django.urls import path

from storage.views import StorageHomeView, SnapshotHomeView, SnapshotDetailView, SnapshotAddView

app_name = 'storage'

urlpatterns = [
    path('', StorageHomeView.as_view(), name='index'),
    path('snapshots/', SnapshotHomeView.as_view(), name='snapshots'),
    path('snapshot/<int:pk>/', SnapshotDetailView.as_view(), name='snapshot_detail'),
    path('snapshot/add/', SnapshotAddView.as_view(), name='snapshot_add'),
]
