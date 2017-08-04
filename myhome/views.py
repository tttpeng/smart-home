from django.http import HttpResponse
from .player import Player
from django.views.decorators.csrf import csrf_protect


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


def resource(request):
    print(request.body.decode(encoding='UTF-8'))
    if request.body.decode(encoding='UTF-8') == 'ON':
        print('ppplay')
        Player().play()
        if not Player().check_music_play():
            Player().switch_play_status()
        print(request)
    if request.body.decode(encoding='UTF-8') == 'OFF':
        print('sttttpop')
        if Player().check_music_play():
            Player().switch_play_status()

    is_play = Player().check_music_play()
    return HttpResponse("ON" if is_play else "OFF")
