import subprocess
import threading
from .singleton import Singleton


class Player(metaclass=Singleton):
    def __init__(self):
        self.p = None

    def playok(self):
        r = subprocess.call(
            ['open', '/Users/tpeng/Desktop/playNeteaseMusicFM.app'])
        print('Exit code:', r)

    def play(self, words):
        t = threading.Thread(target=self.playok)
        t.start()

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
