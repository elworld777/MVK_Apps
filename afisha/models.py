from django.db import models
from django.db.models import Q
from datetime import date
from django.utils.functional import cached_property


# class EntryManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(Q(active=True), Q(date_end__gte=date.today() | Q(date_end=None))


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    active = models.BooleanField("Активность", default=True)
    icon = models.ImageField(
        "Иконка", null=True, blank=True, upload_to="icon/")
    url = models.SlugField("Ссылка", max_length=160, unique=True)
    num = models.PositiveSmallIntegerField(
        "Номер выводимой записи", null=True, blank=True)
    parent_category = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Родительская категория')
    priority = models.PositiveSmallIntegerField(
        "Приоритет", default=10, null=True, blank=True)
    text = models.TextField("Описание", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Entry(models.Model):
    title = models.CharField("Название", max_length=150)
    active = models.BooleanField("Активность", default=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    preview = models.ImageField("Превью", upload_to="preview/")
    detail = models.ImageField(
        "Детальная картинка", upload_to="detail/", null=True, blank=True)
    width = models.PositiveSmallIntegerField("Ширина", default=1)
    date_start = models.DateField("Дата начала", null=True, blank=True)
    date_end = models.DateField("Дата окончания", null=True, blank=True)
    duration = models.TextField("Продолжительность", null=True, blank=True)
    price = models.TextField("Цены", null=True, blank=True)
    text = models.TextField("Описание")
    # objects = EntryManager()

    def __str__(self):
        return self.title

    @cached_property
    def is_active(self):
        if self.date_end is None:
            return True
        else:
            if self.date_end >= date.today() and self.active:
                return True
        return False

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


class Dates(models.Model):
    date_start = models.DateField("Дата начала", null=True, blank=True)
    date_end = models.DateField("Дата окончания", null=True, blank=True)
    entry_dates = models.ForeignKey(
        Entry, on_delete=models.CASCADE, related_name='entry_dates')


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
