from django.contrib import admin
from afisha.models import Category, Entry, Gallery, Exhibit, Setting

admin.site.register(Setting)
admin.site.register(Exhibit)


class GalleryInline(admin.TabularInline):
    fk_name = 'images'
    model = Gallery


@admin.register(Entry)
class ImagesAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]


admin.site.register(Category)
