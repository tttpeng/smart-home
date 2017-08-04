import subprocess
import threading
from .singleton import Singleton


class Player(metaclass=Singleton):
    def playok(self):
        data = open('AppleScript/playNeteaseMusicFM.applescript')
        text = data.read()
        self.asrun(text.encode(encoding='UTF-8')).decode(encoding='UTF-8')

    def play(self):
        thread = threading.Thread(target=self.playok)
        thread.start()

    def check_music_play(self):
        data = open('AppleScript/checkPlayStatus.applescript')
        text = data.read()
        is_play = bool(
            int(
                self.asrun(text.encode(encoding='UTF-8')).decode(
                    encoding='UTF-8')))
        print('isplay', is_play)
        return is_play

    def asrun(self, ascript):
        osa = subprocess.Popen(
            ['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return osa.communicate(ascript)[0]

    def switch_play_status(self):
        data = open('AppleScript/switchPlayStatus.applescript')
        text = data.read()
        print('switch')
        self.asrun(text.encode(encoding='UTF-8')).decode(encoding='UTF-8')
