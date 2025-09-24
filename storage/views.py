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
        error_list = {}
        s = open('storage/utils/print_list.csv', encoding='utf-8').read()
        temp_list = s.split('\n')
        title_list = temp_list.pop(0)
        for idx, i in enumerate(temp_list):
            if idx != 0:
                if i != '':
                    a = i.split(';')
                    a[0] = a[0].zfill(11)
                    if a[2] == '':
                        a[2] = 0
                    else:
                        try:
                            a[2] = int(a[2])
                        except ValueError:
                            print(f"{a[0]} - {a[2]} - не число!")
                            error_list[a[0]] = a
                            a[2] = 0
                    if a[2] > 0:
                        a[2] = range(0, a[2])
                        print(a[2])
                        print_list[a[0]] = a
        context['title_list'] = title_list
        context['error_list'] = error_list
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