from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, PlaceImage


def preview_inline(obj):
    if obj.image:
        return format_html(
            '<img src="{}" style="max-width: 300px; max-height: 200px" />',
            obj.image.url
        )
    return format_html('<span style="color: red;">Изображение не загружено</span>')


class AdminInLine(SortableTabularInline):
    model = PlaceImage
    can_delete = False
    extra = 0
    fields = (('image', preview_inline))
    readonly_fields = [preview_inline,]
    verbose_name_plural = 'Фотографии'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title',]
    inlines = [AdminInLine]

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    def preview(obj):
        return format_html(
            '<img src="{}" style="max-width: 300px; max-height: 200px" />',
            obj.image.url
            )

    list_display = ['place',]
    raw_id_fields = ['place',]
    readonly_fields = [preview,]
