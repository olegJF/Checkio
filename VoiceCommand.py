class VoiceCommand:
    
    def __init__(self, channels):
        self.channels = channels
        self.program = 0
        self.size = len(channels) - 1

    def first_channel(self):
        self.program = 0
        return self.channels[0]

    def last_channel(self):
        self.program = self.size
        return self.channels[self.program]

    def turn_channel(self, n):
        self.program = n-1
        return self.channels[n-1]

    def next_channel(self):
        tmp = self.program + 1
        self.program = tmp if tmp <= self.size else 0
        return self.channels[self.program]

    def previous_channel(self):
        tmp = self.program -1
        self.program =  self.size if tmp < 0 else tmp
        return self.channels[self.program]

    def current_channel(self):
        return self.channels[self.program]

    def is_exist(self, ch):
        if isinstance(ch, int):
            return 'Yes' if ch > 0 and ch <= self.size else 'No'
        return 'Yes' if ch in self.channels else 'No'
                
##
##
##if __name__ == '__main__':
##    #These "asserts" using only for self-checking and not necessary for auto-testing
##
##    CHANNELS = ["BBC", "Discovery", "TV1000"]
##
##    controller = VoiceCommand(CHANNELS)
##    
##    assert controller.first_channel() == "BBC"
##    assert controller.last_channel() == "TV1000"
##    assert controller.turn_channel(1) == "BBC"
##    assert controller.next_channel() == "Discovery"
##    assert controller.previous_channel() == "BBC"
##    assert controller.current_channel() == "BBC"
##    assert controller.is_exist(4) == "No"
##    assert controller.is_exist("TV1000") == "Yes"
##    print("Coding complete? Let's try tests!")
