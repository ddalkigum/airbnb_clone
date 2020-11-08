from django.shortcuts import render
from .models import Room


def room_view(request):
    if request.method == "GET":
        rooms = Room.objects.all()

        return render(
            request,
            "base.html",
            context={
                "rooms": rooms,
            },
        )
