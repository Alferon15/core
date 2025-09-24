from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cartridge, Snapshot
from .forms import SnapshotAddForm, CartidgeLoadPrintListForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View, FormView


class CartridgeRefreshView(View):
    def get(self, request, *args, **kwargs):
        cart_file = open('storage/utils/list.csv')
        cart_str = cart_file.read()
        cart_file.close()
        cart_list = cart_str.split('\n')
        cartridges_db = Cartridge.objects.all()
        for c in cart_list:
            if c != '' and len(c) == 3:
                s = c.split(';')
                cart = cartridges_db.filter(number=s[0]).exists()
                if not cart:
                    print(s[0])
                    cart = Cartridge(number=s[0], article=s[1], caption=s[2])
                    cart.save()
        return redirect('storage:cartridge_list')


class CartridgeListView(ListView):
    model = Cartridge
    queryset = Cartridge.objects.all()


class CartridgeLoadPrintListView(FormView):
    form_class = CartidgeLoadPrintListForm
    template_name = 'storage/cartridge_load_print_list.html'
    
    def post(self, request, *args, **kwargs):
        file_upload = request.FILES['file_upload']
        with open('storage/utils/print_list.csv', "wb+") as destination:
            for chunk in file_upload.chunks():
                destination.write(chunk)
        return redirect('storage:barcode_list')


class CartridgeBarcodeListView(TemplateView):
    template_name = 'storage/cartridge_barcode_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print_list = {}
        s = open('storage/utils/print_list.csv').read()
        temp_list = s.split('\n')
        for i in temp_list:
            a = i.split(';')
            print_list[a[0]] = a
        context['print_list'] = print_list
        return context

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