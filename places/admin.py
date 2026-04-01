from django.contrib import admin
from places import models


class PlaceImageInline(admin.TabularInline):
    model = models.PlaceImage
    extra = 1


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
