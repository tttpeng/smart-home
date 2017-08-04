from django.http import HttpResponse
from .player import Player


def play(request):
    print(request)
    Player().play()
    if not Player().check_music_play():
        Player().switch_play_status()
    return HttpResponse("0")


def pause(request):
    print(request)
    if Player().check_music_play():
        Player().switch_play_status()
    return HttpResponse("0")


def check(request):
    print(request)
    is_play = Player().check_music_play()
    return HttpResponse(1 if is_play else 0)
