from django import forms
from .models import Snapshot


class SnapshotAddForm(forms.ModelForm):
    dt = forms.DateField(label='Дата инвентаризации', widget=forms.SelectDateWidget, required=True)
    item_list = forms.CharField(label='Список картриджей', widget=forms.Textarea, required=True)
    
    class Meta:
        model = Snapshot
        fields = ['dt']


class CartidgeLoadPrintListForm(forms.Form):
    file_upload = forms.FileField(label='Файл')
    
    class Meta:
        fields = ['file_path', 'file']