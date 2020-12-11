from django.contrib import admin
from .models import Titles, Genres, Categories


# Register your models here.
class TitlesAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "description")

    def __str__(self):
        return self.name


admin.site.register(Titles, TitlesAdmin)
admin.site.register(Genres)
admin.site.register(Categories)