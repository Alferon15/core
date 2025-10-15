from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cartridge, Snapshot, Item
from .forms import SnapshotAddForm, LoadFileForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View, FormView

from datetime import date
from .utils.utils import do_count


class CartridgeRefreshView(LoginRequiredMixin, View):
    template_name = 'storage/cartridge_refresh_list.html'
    
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


class CartridgeRefreshListView(LoginRequiredMixin, TemplateView, FormView):
    form_class = LoadFileForm
    template_name = 'storage/cartridge_refresh_list.html'

    def post(self, request, *args, **kwargs):
        file_upload = request.FILES['file_upload']
        f = file_upload.read().decode('utf-8')
        temp_str = f.split('\n')
        temp_str.pop(0)
        for s in temp_str:
            if s != '':
                l = s.split(';')
                if l[0] != '':
                    v = int(l[0])
                    if v > 0:
                        num = l[0].zfill(11)
                        print(num)
        return redirect('storage:cartridge_refresh')


class CartridgeListView(ListView):
    model = Cartridge
    queryset = Cartridge.objects.all()


class CartridgePrintListView(LoginRequiredMixin, TemplateView):
    template_name = 'storage/cartridge_print_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cartridges = Cartridge.objects.all()
        context["cartridges"] = cartridges
        return context
    
    def post(self, request, *args, **kwargs):
        cartridges = Cartridge.objects.all()
        count = request.POST.copy()
        count.pop('csrfmiddlewaretoken')
        data = {}
        for k, v in count.items():
            if v != '':
                v = int(v)
                if v > 0:
                    article = cartridges.get(number=k).article
                    caption = cartridges.get(number=k).caption
                    data[k] = {'number':k, 'article':article, 'count':'c'*v, 'caption':caption}
        request.session['data'] = data
        return redirect('storage:print_barcode')


class CartridgePrintListFileView(LoginRequiredMixin, FormView):
    form_class = LoadFileForm
    template_name = 'storage/cartridge_print_list_file.html'

    def post(self, request, *args, **kwargs):
        file_upload = request.FILES['file_upload']
        f = file_upload.read().decode('utf-8')
        data = {}
        temp_str = f.split('\n')
        temp_str.pop(0)
        for s in temp_str:
            if s != '':
                l = s.split(';')
                if l[2] != '':
                    v = int(l[2])
                    if v > 0:
                        num = l[0].zfill(11)
                        data[num] = {'number':num, 'article':l[1], 'count':'c'*v, 'caption':l[3]}
        request.session['data'] = data
        return redirect('storage:print_barcode')
        

class CartridgePrintBarcodeView(LoginRequiredMixin, TemplateView):
    template_name = 'storage/cartridge_print_barcode.html'


class StorageHomeView(TemplateView):
    template_name = 'storage/storage_home.html'


class SnapshotHomeView(ListView):
    model = Snapshot
    queryset = Snapshot.objects.all()
    template_name = 'storage/snapshot_home.html'


class SnapshotAddView(LoginRequiredMixin, CreateView):
    form_class = SnapshotAddForm
    template_name = 'storage/snapshot_add.html'

    def post(self, request, *args, **kwargs):
        temp_list = request.POST.copy()
        temp_list.pop('csrfmiddlewaretoken')
        snap = Snapshot()
        snap.dt = date(int(temp_list['dt_year']), int(temp_list['dt_month']), int(temp_list['dt_day']))
        snap.save()
        items = temp_list['item_list'].split('\r\n')
        c_list = do_count(items)
        all_cartridges = Cartridge.objects.all()
        for i in c_list.values():
            c = all_cartridges.get(number=i['number'])
            if c:
                cur_item = Item()
                cur_item.cartridge = c
                cur_item.count = i['count']
                cur_item.snapshot = snap
                cur_item.save()
            else:
                print('Нет ' + i)
        return redirect('storage:snapshot_detail', snap.id)


class SnapshotDetailView(DetailView):
    model = Snapshot
    template_name = 'storage/snapshot_detail.html'