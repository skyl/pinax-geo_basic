# admin.py

from django.contrib import admin
from olwidget.admin import GeoModelAdmin
from attractions.models import AreaDescription, Area, Attraction, Hotel, Headline

class AreaAdmin(GeoModelAdmin):
    options = {
        'default_lat': -34.0,
        'default_lon': 18.4,
        'default_zoom': 9,
    }
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug','get_attractions',
        'attraction_tags',
    )
    list_map = ('poly_simplify',)
    list_map_options = {
        'cluster_display': 'list',
        'default_lat': -34.0,
        'default_lon': 18.4,
        'default_zoom': 9,
    }
    list_filter = ('featured',)

class AttractionAdmin(GeoModelAdmin):
    options = {
        #'layers': ['osm.mapnik', 'google.hybrid', 'google.streets'],
        'default_lat': -34.0,
        'default_lon': 18.4,
        'default_zoom': 9,
    }
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug',
            #'url','email', 'street_address', 'locality',
            #'region', 'postal_code', 'country', 'tel_work', 'tel_home',
            'tags','get_areas')
    list_map = ('point',)

    list_map_options = {
        # group nearby points into clusters
        'cluster': True,
        'cluster_display': 'list',
        'default_lat': -34.0,
        'default_lon': 18.4,
        'default_zoom': 9,
    }

class HotelAdmin(GeoModelAdmin):
    options = {
        'default_lat': -34.0,
        'default_lon': 18.4,
        'default_zoom': 7,
    }
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug',)
    list_map = ('point',)

    list_map_options = {
        # group nearby points into clusters
        'layers': ['osm.mapnik', 'google.hybrid', 'google.streets'],
        'cluster': True,
        'cluster_display': 'list',
        'default_lat': -34.0,
        'default_lon': 18.4,
        'default_zoom': 5,
    }

admin.site.register(Headline, HeadlineAdmin)
admin.site.register(AreaDescription, AreaDescriptionAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Attraction, AttractionAdmin)
admin.site.register(Hotel, HotelAdmin)
