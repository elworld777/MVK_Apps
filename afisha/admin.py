from django.contrib import admin
from afisha.models import Category, Entry, Gallery, Dates, Exhibit, Setting

admin.site.register(Setting)
admin.site.register(Exhibit)


class GalleryInline(admin.TabularInline):
    fk_name = 'images'
    model = Gallery

class DatesInline(admin.TabularInline):
    fk_name = 'entry_dates'
    model = Dates

@admin.register(Entry)
class ImagesAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, DatesInline]


admin.site.register(Category)
