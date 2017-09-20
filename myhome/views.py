from django.http import HttpResponse
from .player import Player
from django.views.decorators.csrf import csrf_protect
from myhome.tasks import check
import requests
from bs4 import BeautifulSoup


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


def check_apple_watch(request):
    url = "https://www.apple.com/cn/watch/cellular/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    string = soup.find(
        href="http://wap.10010.com/t/operationservice/QualificationCheck.htm"
    ).find_next_siblings("span")[0].contents[0]
    print(string)
    if string != '蜂窝网络服务仅适用于归属地为上海、广东、河南、湖南和天津的手机账号1':
        payload = {
            "msgtype": "text",
            "text": {
                "content": "Apple Watch 抢购啦！---" + string
            }
        }
        headers = {'content-type': 'application/json'}
        r2 = requests.post(
            'https://oapi.dingtalk.com/robot/send?access_token=d433573e5ad18c36de2957406993fe1b78da0cbf64dd4e361c1746cfc0d0e223',
            json=payload,
            headers=headers)
        print(r2.text)

    return HttpResponse("ok")
