"""

"""
from django.http import HttpResponse
from .player import Player
from django.http import JsonResponse

def index(request):
    words = request.GET.get('words')
    if words:
        Player().play(words)
        return JsonResponse({'status':bool(1)})
    else:
        return JsonResponse({'status':bool(0)})


def pause(request):
    Player().pause()
    return HttpResponse("Hello, world. You're at the polls index.")


def quit(request):
    Player().quite()
    return HttpResponse("haha")
