# Standard scientific Python imports
import time

import sys
from naoqi import ALProxy, ALBroker
from NaoTextEvent import NaoTextEventModule


def main():
    mybroker = ALBroker("myBroker",
                        "0.0.0.0",  # listen to anyone
                        0,  # find a free port and use it
                        "127.0.0.1",  # parent broker IP
                        39274)  # parent broker port
    global NaoTextEvent
    NaoTextEvent = NaoTextEventModule("NaoTextEvent")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        mybroker.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    main()