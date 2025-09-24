from django import forms
from .models import Snapshot, Cartridge

from .utils.utils import do_count


class SnapshotAddForm(forms.ModelForm):
    dt = forms.DateField(label='Дата инвентаризации', widget=forms.SelectDateWidget, required=True)
    item_list = forms.CharField(label='Список картриджей', widget=forms.Textarea, required=True)
    
    class Meta:
        model = Snapshot
        fields = ['dt']

    def clean_item_list(self):
        item_list = self.cleaned_data['item_list']
        items = item_list.split('\n')
        temp_list = do_count(items)
        all_cartridges = Cartridge.objects.all()
        for i in temp_list:
            if all_cartridges.filter(number=i).exists():
                print('Есть ' + i)
            else:
                print('Нет ' + i)
        return item_list


class CartidgeLoadPrintListForm(forms.Form):
    file_upload = forms.FileField(label='Файл')
    
    class Meta:
        fields = ['file_path', 'file']