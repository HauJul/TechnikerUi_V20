from gpiozero.pins.rpigpio import RPiGPIOFactory
from gpiozero import Device, DigitalInputDevice


class Toolbox:
    def __init__(self):
        # Set PinFactory for virtual Environment
        Device.pin_factory = RPiGPIOFactory()
        # Output Toolbox
        self.outBit0 = DigitalInputDevice(16, pull_up=True)
        self.outBit1 = DigitalInputDevice(17, pull_up=True)
        self.outBit2 = DigitalInputDevice(18, pull_up=True)

    # Read outputs of Toolbox and format binary code to integer value
    def get_tool(self):
        bit0 = self.outBit0.value
        bit1 = self.outBit1.value
        bit2 = self.outBit2.value

        tool = bit0 + 2 * bit1 + 4 * bit2

        return tool
