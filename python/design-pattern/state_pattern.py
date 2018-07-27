from abc import ABC, abstractmethod


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


class Phone:
    def __init__(self):
        self.s = SoundState()

    def incomingCall(self):
        self.s.ring()

    def volumeUp(self):
        self.s = self.s.nextStateVolumeUp()

    def volumeDown(self):
        self.s = self.s.nextStateVolumeDown()


p = Phone()
p.incomingCall()
p.volumeUp()
p.incomingCall()
p.volumeDown()
p.incomingCall()
p.volumeDown()
p.incomingCall()
p.volumeUp()
p.incomingCall()
