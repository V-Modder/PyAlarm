import time

# pip install python-vlc
from vlc import MediaPlayer

class AlarmPlayer:
    def __init__(self):
        self.__radioStreamUrl = "http://188.94.97.91:80/radio21.mp3"
        self.__backupFile = "backup.mp3"
        self.__player = None

    def play(self):
        self.__player = MediaPlayer(self.__radioStreamUrl)
        self.setVolume(0)
        self.__player.play()
        time.sleep(1)
        if self.__player.is_playing() == 0:
            self.__player = MediaPlayer(self.__backupFile)
            self.setVolume(0)
            self.__player.play()            
    
    def stop(self):
        self.__player.stop()
    
    def setVolume(self, volume):
        if volume < 0 or volume > 100:
            raise("Volume must bw a numeric between 0 and 100")
        self.__player.audio_set_volume(volume)

    def getVolume(self):
        return self.__player.audio_get_volume()

    def increaseVolume(self, step=1, maxVolume=100):
        if self.getVolume() + step < maxVolume:
            self.setVolume(self.getVolume() + step)
        elif self.getVolume() < maxVolume:
            self.setVolume(maxVolume)

