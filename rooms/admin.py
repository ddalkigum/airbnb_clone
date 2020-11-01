from django.contrib import admin
from .models import Room, Amenity, Facility, HouseRule, RoomType


@admin.register(Amenity, Facility, HouseRule, RoomType)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                    "instant_book",
                ),
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "beds",
                    "bedrooms",
                    "baths",
                    "guests",
                ),
            },
        ),
        (
            "More",
            {
                "fields": (
                    "amenities",
                    "facilities",
                    "house_rules",
                ),
            },
        ),
        (
            "last_detail",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "beds",
        "bedrooms",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
    )

    search_fields = (
        "city",
        "host__username",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )