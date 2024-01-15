from gpiozero.pins.rpigpio import RPiGPIOFactory
from gpiozero import Device, DigitalInputDevice, DigitalOutputDevice


class CVIR:
    def __init__(self):
        # Set PinFactory for virtual Environment
        Device.pin_factory = RPiGPIOFactory()
        # Inputs CVIR2
        self.inZYK1 = DigitalOutputDevice(0)
        self.inZYK2 = DigitalOutputDevice(1)
        self.inZYK4 = DigitalOutputDevice(2)
        self.inSPFREI = DigitalOutputDevice(3)
        self.inNIOQUT = DigitalOutputDevice(4)
        self.inSTART = DigitalOutputDevice(5)
        self.inLOESEN = DigitalOutputDevice(6)
        self.inRESET = DigitalOutputDevice(7)

        # Outputs CVIR 2
        self.outZYK1 = DigitalInputDevice(8, pull_up=True)
        self.outZYK2 = DigitalInputDevice(9, pull_up=True)
        self.outZYK4 = DigitalInputDevice(10, pull_up=True)
        self.outBEREIT = DigitalInputDevice(11, pull_up=True)
        self.outZLAEUF = DigitalInputDevice(12, pull_up=True)
        self.outIO = DigitalInputDevice(13, pull_up=True)
        self.outNIO = DigitalInputDevice(14, pull_up=True)
        self.outIOZ = DigitalInputDevice(15, pull_up=True)

        # Outputs Hand Control Element
        self.outSF1 = DigitalInputDevice(19, pull_up=True)
        self.outSF2 = DigitalInputDevice(20, pull_up=True)

        self.step = 0

        # Interupt Hand Control Element
        self.outSF1.when_activated = self.__button_press
        self.outSF1.when_deactivated = self.__button_release
        self.outSF2.when_activated = self.__button_press
        self.outSF2.when_deactivated = self.__button_release

    def set_cyc(self, cyc):
        scyc = format(cyc, "b").zfill(3)
        if scyc[2] == "0":
            self.inZYK1.off()
        else:
            self.inZYK1.on()
        if scyc[1] == "0":
            self.inZYK2.off()
        else:
            self.inZYK2.on()
        if scyc[0] == "0":
            self.inZYK4.off()
        else:
            self.inZYK4.on()

    def release_start(self):
        self.inSPFREI.on()

    def lock_start(self):
        self.inSPFREI.off()

    def __button_press(self):
        state_sf1 = self.outSF1.value
        state_sf2 = self.outSF2.value
        # Reset input
        if state_sf2 and state_sf1:
            self.inRESET.on()
            self.inSTART.off()
            self.inLOESEN.off()
        # Start input
        elif state_sf1 and not state_sf2:
            self.inSTART.on()
        #Release input
        elif state_sf2 and not state_sf1:
            self.inLOESEN.on()
            self.inSTART.on()


    def __button_release(self):
        state_sf1 = self.outSF1.value
        state_sf2 = self.outSF2.value
        if not state_sf1:
            self.inSTART.off()
            self.inRESET.off()
        if not state_sf2:
            self.inLOESEN.off()
            self.inRESET.off()
