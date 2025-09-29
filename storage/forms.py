from django import forms
from .models import Snapshot, Cartridge, Item

from .utils.utils import do_count


class SnapshotAddForm(forms.ModelForm):
    dt = forms.DateField(label='Дата инвентаризации', widget=forms.SelectDateWidget, required=True)
    item_list = forms.CharField(label='Список картриджей', widget=forms.Textarea, required=True)
    
    class Meta:
        model = Snapshot
        fields = ['dt']

    def clean_item_list(self):
        item_list = self.cleaned_data['item_list']
        items = item_list.split('\r\n')
        temp_list = do_count(items)
        all_cartridges = Cartridge.objects.all()
        print(temp_list)
        for i, v in temp_list:
            c = all_cartridges.get(number=i)
            print(i, v)
            if c:
                cur_item = Item()
                cur_item.cartridge = c
                cur_item.count = i[i]
                cur_item.snapshot = self.instance
            else:
                print('Нет ' + i)
        return item_list


class CartidgeLoadPrintListForm(forms.Form):
    file_upload = forms.FileField(label='Файл')
    
    class Meta:
        fields = ['file_path', 'file']