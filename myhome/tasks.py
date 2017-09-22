from celery import shared_task
import requests
from bs4 import BeautifulSoup
import json


@shared_task
def check():
    print("check----run------go")
    url = "https://www.apple.com/cn/watch/cellular/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    string = soup.find(
        href="http://wap.10010.com/t/operationservice/QualificationCheck.htm"
    ).find_next_siblings("span")[0].contents[0]
    if string != '蜂窝网络服务仅适用于归属地为上海、广东、河南、湖南和天津的手机账号':
        print('ddd-----ddddd')
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
    return string


@shared_task
def celery_test():
    string = "哈哈"
    # .encode(encoding='unicode_escape').decode('unicode_escape')
    # .decode('')
    print("----" + string + "----")

    return string
