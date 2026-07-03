from audi_can.bus import CANBus
from audi_can.mfsw import MFSW
from audi_can.mfsw.constants import MFSWButtonEvent


comfort_can = CANBus("can0")
mfsw = MFSW(comfort_can)

try:
    while True:
        event = mfsw.listen_buttons()

        match event:
            case MFSWButtonEvent.WHEEL_LEFT_UP:
                print('MFSW: Left scroll up')
            case MFSWButtonEvent.WHEEL_LEFT_DOWN:
                print('MFSW: Left scroll down')
            case MFSWButtonEvent.WHEEL_LEFT_CLICK:
                print('MFSW: Left select short')
            case _:
                if event is not None:
                    print(event) 

except KeyboardInterrupt:
    print('Shutting down comfort can')
    comfort_can.shutdown()