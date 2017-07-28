import subprocess
import threading
from .api import NetEase
from .singleton import Singleton


class Player(metaclass=Singleton):
    def __init__(self):
        self.p = None

    def playok(self, url):
        self.p = subprocess.Popen(
            ["mpg123", '-R'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.p.stdin.write(b'L ' + url.encode('utf-8') + b'\n')
        self.p.stdin.flush()
        while True:
            strout = self.p.stdout.readline().decode('utf-8')


    def search(self, txt):
        netease = NetEase()
        data = netease.search(txt)
        song_ids = []
        print(data)
        if 'songs' in data['result']:
            if 'mp3Url' in data['result']['songs']:
                songs = data['result']['songs']
            else:
                for i in range(0, len(data['result']['songs'])):
                    song_ids.append(data['result']['songs'][i]['id'])
                    songs = netease.songs_detail(song_ids)
                    return netease.dig_info(songs, 'songs')


    def play(self,words):
        self.stop()
        songs = self.search(words)
        song_id = songs[0]['song_id']        
        new_url = NetEase().songs_detail_new_api([song_id])[0]['url']
        t = threading.Thread(target=self.playok,args=(new_url,))
        t.start()

    def change(self):
        print(self.haha)
        self.haha = 'cccc';
        print(self.haha)


    def pause(self):
        self.p.stdin.write(b'P\n')
        self.p.stdin.flush()

    def stop(self):
        if self.p:
            try:
                self.p.stdin.write(b'Q\n')
                self.p.stdin.flush()
                self.p.kill()
            except IOError as e:
                print(e)


    def quite(self):
        self.p.kill()
