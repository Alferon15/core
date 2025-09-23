from django.db import models
from django.urls import reverse


class Cartridge(models.Model):
    number = models.CharField(verbose_name='Номенклатура', primary_key=True, unique=True)
    article = models.CharField(verbose_name='Артикул', unique=True)
    caption = models.TextField(verbose_name='Описание', blank=True, default='')
    
    
    def __str__(self):
        return self.article


    def get_absolute_url(self):
        return reverse("storage:cartidge_detail", kwargs={"pk": self.pk})


class Snapshot(models.Model):
    dt = models.DateField(verbose_name='Дата инвентаризации', unique=True, auto_created=True)


    def __str__(self):
        return self.dt.strftime('%Y-%m-%d')


    def get_absolute_url(self):
        return reverse("storage:snapshot_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    cartridge = models.ForeignKey(Cartridge, verbose_name='Картридж', on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(verbose_name='Количество', default=0)
    snapshot = models.ForeignKey(Snapshot, verbose_name='Снимок', on_delete=models.CASCADE, related_name='items', blank=True)


    def __str__(self):
        return self.cartridge.article


    def get_absolute_url(self):
        return reverse("storage:item_detail", kwargs={"pk": self.pk})




class Printer(models.Model):
    name = models.CharField(verbose_name='Имя принтера')