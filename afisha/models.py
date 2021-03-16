from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    icon = models.ImageField(
        "Иконка", null=True, blank=True, upload_to="icon/")
    url = models.SlugField("Ссылка", max_length=160, unique=True)
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Родительская категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Entry(models.Model):
    title = models.CharField("Название", max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    preview = models.ImageField("Превью", upload_to="preview/")
    detail = models.ImageField("Детальная картинка", upload_to="detail/")
    width = models.PositiveSmallIntegerField("Ширина", default=1)
    date_start = models.DateField("Дата начала", null=True, blank=True)
    date_end = models.DateField("Дата окончания", null=True, blank=True)
    duration = models.TextField("Продолжительность", null=True, blank=True)
    price = models.TextField("Цены")
    text = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Gallery(models.Model):
    image = models.ImageField("Изображение", upload_to='gallery/')
    images = models.ForeignKey(
        Entry, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"


class Exhibit(models.Model):
    name = models.CharField("Название", max_length=150)
    image = models.ImageField("Изображение", upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонаты"

class Setting(models.Model):
    exhibit = models.ForeignKey(
        Exhibit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Экспонат')

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"
