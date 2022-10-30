class TV:
    def __init__(self):
        # self.channel = list(range(1, 121))[0]
        # self.volume = list(range(1, 8))[0]
        # self.on = bool

        #  encalpsulating channel and volume attributes
        self.__channel = 0
        self.__volume = 0
        self.on = False

    # def __repr__(self):
    #     return TV

    def turnOn(self):
        self.on = True
        return 'TV is turning on'#, self.on

    def turnOff(self):
        self.on = False
        return 'TV is turning off'#, self.on

    @property  
    def channel(self):
        print('Current Channel: ', self.__channel)
        return self.__channel
    
    @channel.setter
    def channel(self, channel_no: int):
        if channel_no not in range(1, 121):
            print("Invalid channel")
        else:
            self.__channel = channel_no
    # current channel (1 to 120)
    # def setChannel(self, channel):
    #     self.channel = channel
        
    @property    
    def volume(self):
        print("current volume", self.__volume)
        return self.__volume

    @volume.setter
    def volume(self, volume: int):
        if volume not in range(1, 8):
            print("Invalid volume")
        else:
            self.__volume = volume

    def channelUp(self):
        self.__channel += 1
        print('Channel Increased: ', self.__channel)

    def channelDown(self):
        self.__channel -= 1
        print('Channel Decreased: ', self.__channel)

    def volumeUp(self):
        self.__volume += 1
        print('Volume Increased: ', self.__volume)

    def volumeDown(self):
        self.__volume -= 1
        print('Volume Decreased: ', self.__volume)

# Instance of TV class
tv = TV()
tv.channel = 121
tv.volume =12
tv.volume
tv.channel
# Method operations on the instance