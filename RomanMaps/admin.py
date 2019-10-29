from django.contrib import admin
from RomanMaps.models import Maps, Gallery
    
# admin.site.register(Maps)

class GalleryInline(admin.TabularInline):
    fk_name = 'maps'
    model = Gallery

@admin.register(Maps)
class MapsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]