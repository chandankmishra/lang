from abc import ABC, abstractmethod

# State abstract class


class RingState(ABC):
    @abstractmethod
    def ring(self):
        raise ImplementationError

    def nextStateVolumeUp(self):
        raise ImplementationError

    def nextStateVolumeDown(self):
        raise ImplementationError


class SoundState(RingState):
    def ring(self):
        print ("Phone is ringing")

    def nextStateVolumeUp(self):
        return self

    def nextStateVolumeDown(self):
        return VibrateState()


class VibrateState(RingState):
    def ring(self):
        print ("Phone is vibrating")

    def nextStateVolumeUp(self):
        return SoundState()

    def nextStateVolumeDown(self):
        return SilentState()


class SilentState(RingState):
    def ring(self):
        print (".....")

    def nextStateVolumeUp(self):
        return VibrateState()

    def nextStateVolumeDown(self):
        return self

# Context Class - single interface to the outside world


class Phone:
    def __init__(self):
        self.state = SoundState()

    def incomingCall(self):
        print ("Incoming call")
        self.state.ring()

    def volumeUp(self):
        print ("Incrase volume")
        self.state = self.state.nextStateVolumeUp()

    def volumeDown(self):
        print ("Decrease volume")
        self.state = self.state.nextStateVolumeDown()


p = Phone()
p.incomingCall()
print ('-' * 50)
p.volumeUp()
p.incomingCall()
print ('-' * 50)
p.volumeDown()
p.incomingCall()
print ('-' * 50)
p.volumeDown()
p.incomingCall()
print ('-' * 50)
p.volumeUp()
p.incomingCall()
