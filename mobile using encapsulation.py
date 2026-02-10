class Mobile:
    def __init__(self):
       self._volume=50
    def increase_volume(self):
        if self._volume<100:
           self._volume+=10
        else:
            print("the volume is already maximum")
    def decrease_volume(self):
        if self._volume>0:
            self._volume-=10
        else:
            print("the volume is minimum")
    def mute(self):
        self._volume=0
    def get_volume(self):
        return self._volume
s1=Mobile()
print(s1.get_volume)
s1.increase_volume()
print(s1.get_volume())
s1.decrease_volume()
print(s1.get_volume())
s1.mute()
print(s1.get_volume())
