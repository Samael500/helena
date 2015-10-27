from django.contrib import admin
from content.models import Genres


class GenresAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'description')


admin.site.register(Genres, GenresAdmin)
