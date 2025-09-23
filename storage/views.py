from django.shortcuts import render
from .models import Snapshot
from .forms import SnapshotAddForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView


class StorageHomeView(TemplateView):
    template_name = 'storage/storage_home.html'


class SnapshotHomeView(ListView):
    model = Snapshot
    queryset = Snapshot.objects.all()
    template_name = 'storage/snapshot_home.html'


class SnapshotAddView(CreateView):
    form_class = SnapshotAddForm
    template_name = 'storage/snapshot_add.html'


class SnapshotDetailView(DetailView):
    model = Snapshot
    template_name = 'storage/snapshot_detail.html'