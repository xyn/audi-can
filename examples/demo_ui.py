from audi_can.bus import CANBus
from audi_can.mfsw.constants import MFSWButtonEvent
from audi_can.rnse import RNSE
from audi_can.mfsw import MFSW
from audi_can.rnse.constants import RNSEButtonEvent

comfort_can = CANBus("can0")
rnse = RNSE(comfort_can)
mfsw = MFSW(comfort_can)

try:
    rnse.enable_tv_mode()

    while True:
        rnse_buttons = rnse.listen_buttons()
        mfsw_buttons = mfsw.listen_buttons()

        match rnse_buttons:
            case RNSEButtonEvent.SCROLL_LEFT:
                print("RNSE: Scroll left")
            case RNSEButtonEvent.SCROLL_RIGHT:
                print("RNSE: Scroll right")
            case RNSEButtonEvent.SELECT_SHORT:
                print("RNSE: Select short")
            case _:
                if rnse_buttons is not None:
                    print(rnse_buttons)

        match mfsw_buttons:
            case MFSWButtonEvent.WHEEL_LEFT_UP:
                print("MFSW: Scroll up")
            case MFSWButtonEvent.WHEEL_LEFT_DOWN:
                print("MFSW: Scroll down")
            case MFSWButtonEvent.WHEEL_LEFT_CLICK:
                print("MFSW: Click")
            case _:
                if mfsw_buttons is not None:
                    print(mfsw_buttons)

except KeyboardInterrupt:
    print('Shutting down comfort can')
    rnse.disable_tv_mode()
    comfort_can.shutdown()

