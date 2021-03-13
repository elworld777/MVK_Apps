from django.contrib import admin
from afisha.models import Category, Entry, Gallery, Exhibit

admin.site.register(Exhibit)
admin.site.register(Category)

class GalleryInline(admin.TabularInline):
    fk_name = 'images'
    model = Gallery

@admin.register(Entry)
class ImagesAdmin(admin.ModelAdmin):
    inlines = [GalleryInline, ]