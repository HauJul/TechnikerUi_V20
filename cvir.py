from gpiozero import DigitalInputDevice, DigitalOutputDevice

#Inputs CVIR2
inZYK1 = DigitalOutputDevice(0)
inZYK2 = DigitalOutputDevice(1)
inZYK4 = DigitalOutputDevice(2)
inSPFREI = DigitalOutputDevice(3)
inNIOQUT = DigitalOutputDevice(4)
inSTART = DigitalOutputDevice(5)
inLOESEN = DigitalOutputDevice(6)
inRESET = DigitalOutputDevice(7)

#Outputs CVIR 2
outZYK1 = DigitalInputDevice(8, pull_up=True)
outZYK2 = DigitalInputDevice(9, pull_up=True)
outZYK4 = DigitalInputDevice(10, pull_up=True)
outBEREIT = DigitalInputDevice(11, pull_up=True)
outZLAEUF = DigitalInputDevice(12, pull_up=True)
outIO = DigitalInputDevice(13, pull_up=True)
outNIO = DigitalInputDevice(14, pull_up=True)
outIOZ = DigitalInputDevice(15, pull_up=True)

outSF1 = DigitalInputDevice(19, pull_up=True)
outSF2 = DigitalInputDevice(20, pull_up=True)

step = 0




def set_input(inzyk1, inzyk2, inzyk4):
    if inzyk1:
        inZYK1.on()
    else:
        inZYK1.off()
    if inzyk2:
        inZYK2.on()
    else:
        inZYK2.off()
    if inzyk4:
        inZYK4.on()
    else:
        inZYK4.off()


def set_cyc(cyc):
    if cyc == 1:
        set_input(True, False, False)
    elif cyc == 2:
        set_input(False, True, False)
    elif cyc == 3:
        set_input(True, True, False)
    elif cyc == 4:
        set_input(False, False, True)
    else:
        print("Schraubablauf nicht bekannt")    #ToDo Fehlermeldung


def release_start():
    inSPFREI.on()


def lock_start():
    inSPFREI.off()


def button_press():
    state_sf1 = outSF1.value
    state_sf2 = outSF2.value
    if state_sf2 and state_sf1:
        inRESET.on()
        inSTART.off()
        inLOESEN.off()
    elif state_sf1 and not state_sf2:
        inSTART.on()
    elif state_sf2 and not state_sf1:
        inLOESEN.on()


def button_release():
    state_sf1 = outSF1.value
    state_sf2 = outSF2.value
    if not state_sf1:
        inSTART.off()
        inRESET.off()
    if not state_sf2:
        inLOESEN.off()
        inRESET.off()


# Interupt Bedienelement
outSF1.when_activated = button_press
outSF1.when_deactivated = button_release
outSF2.when_activated = button_press
outSF2.when_deactivated = button_release
