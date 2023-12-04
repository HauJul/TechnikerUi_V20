from gpiozero import DigitalInputDevice, DigitalOutputDevice

#Inputs CVIR2
__inZYK1 = DigitalOutputDevice(0)
__inZYK2 = DigitalOutputDevice(1)
__inZYK4 = DigitalOutputDevice(2)
__inSPFREI = DigitalOutputDevice(3)
__inNIOQUT = DigitalOutputDevice(4)
__inSTART = DigitalOutputDevice(5)
__inLOESEN = DigitalOutputDevice(6)
__inRESET = DigitalOutputDevice(7)

#Outputs CVIR 2
__outZYK1 = DigitalInputDevice(8, pull_up=True)
__outZYK2 = DigitalInputDevice(9, pull_up=True)
__outZYK4 = DigitalInputDevice(10, pull_up=True)
__outBEREIT = DigitalInputDevice(11, pull_up=True)
__outZLAEUF = DigitalInputDevice(12, pull_up=True)
__outIO = DigitalInputDevice(13, pull_up=True)
__outNIO = DigitalInputDevice(14, pull_up=True)
__outIOZ = DigitalInputDevice(15, pull_up=True)

__outSF1 = DigitalInputDevice(19, pull_up=True)
__outSF2 = DigitalInputDevice(20, pull_up=True)

step = 0


def set_input(inzyk1, inzyk2, inzyk4):
    if inzyk1:
        __inZYK1.on()
    else:
        __inZYK1.off()
    if inzyk2:
        __inZYK2.on()
    else:
        __inZYK2.off()
    if inzyk4:
        __inZYK4.on()
    else:
        __inZYK4.off()


def set_cyc(cyc):
    if cyc == 1:
        set_input(True, False, False)
        print("Schraubablauf 1")
    elif cyc == 2:
        set_input(False, True, False)
        print("Schraubablauf 2")
    elif cyc == 3:
        set_input(True, True, False)
    elif cyc == 4:
        set_input(False, False, True)
    else:
        print("Schraubablauf nicht bekannt")


def release_start():
    __inSPFREI.on()


def lock_start():
    __inSPFREI.off()


def button_press():
    state_sf1 = __outSF1.value
    state_sf2 = __outSF2.value
    print("Tastendruck erkannt")
    if state_sf2 and state_sf1:
        __inRESET.on()
        __inSTART.off()
        __inLOESEN.off()
        print("Reset ein")
    elif state_sf1 and not state_sf2:
        __inSTART.on()
        print("Start ein")
    elif state_sf2 and not state_sf1:
        __inLOESEN.on()
        print("Loesen ein")


def button_release():
    state_sf1 = __outSF1.value
    state_sf2 = __outSF2.value
    if not state_sf1:
        __inSTART.off()
        __inRESET.off()
        print("Start aus")
    if not state_sf2:
        __inLOESEN.off()
        __inRESET.off()
        print("Loesen aus")