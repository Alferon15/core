from django.db import models
from django.urls import reverse


class Cartridge(models.Model):
    number = models.CharField(verbose_name='Номенклатура', max_length=16, primary_key=True, unique=True)
    article = models.CharField(verbose_name='Артикул', max_length=128)
    caption = models.TextField(verbose_name='Описание', blank=True, default='')
    priority = models.IntegerField(verbose_name='Приоритет', default=0)
    
    class Meta:
        ordering = ["-priority"]
    
    
    def __str__(self):
        return self.number


    def get_absolute_url(self):
        return reverse("storage:cartidge_detail", kwargs={"pk": self.pk})


class Snapshot(models.Model):
    dt = models.DateField(verbose_name='Дата инвентаризации', auto_created=True)


    def __str__(self):
        return self.dt.strftime('%Y-%m-%d')


    def get_absolute_url(self):
        return reverse("storage:snapshot_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    cartridge = models.ForeignKey(Cartridge, verbose_name='Картридж', on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(verbose_name='Количество', default=0)
    snapshot = models.ForeignKey(Snapshot, verbose_name='Снимок', on_delete=models.CASCADE, related_name='items', blank=True)


    def __str__(self):
        return f"{self.cartridge.article} - {self.count}"


    def get_absolute_url(self):
        return reverse("storage:item_detail", kwargs={"pk": self.pk})


class Printer(models.Model):
    name = models.CharField(verbose_name='Имя принтера', max_length=128)