from celery import shared_task
import requests
from bs4 import BeautifulSoup


@shared_task
def check():
    url = "https://www.apple.com/cn/watch/cellular/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    print('------------------')
    string = soup.find(
        href="http://wap.10010.com/t/operationservice/QualificationCheck.htm"
    ).find_next_siblings("span")[0].contents[0]

    return string