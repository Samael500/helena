from django.contrib import admin
from content.models import Genres, Galleries


class GenresAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'description')


class GalleriesAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'img_url')


admin.site.register(Genres, GenresAdmin)
admin.site.register(Galleries, GalleriesAdmin)
