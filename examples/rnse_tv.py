from audi_can.bus import CANBus
from audi_can.rnse import RNSE
from audi_can.rnse.constants import RNSEButtonEvent

comfort_can = CANBus("can0")
rnse = RNSE(comfort_can)



try:
    rnse.enable_tv_mode()

    while True:
        event = rnse.listen_buttons()

        match event:
            case RNSEButtonEvent.SCROLL_LEFT:
                print("RNSE: Scroll left")
            case RNSEButtonEvent.SCROLL_RIGHT:
                print("RNSE: Scroll right")
            case RNSEButtonEvent.SELECT_SHORT:
                print("RNSE: Select short")
            case _:
                if event is not None:
                    print(event)

except KeyboardInterrupt:
    print('Disabling TV Mode and shutting down comfort can')
    rnse.disable_tv_mode()
    comfort_can.shutdown()