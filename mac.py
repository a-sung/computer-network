import random
import time

class Mac:
    def __init__(self):
        self.Kmax = 15
        self.Tfr = 0.000006 # transfer time for a frame: 6us


    def CSMACD(self):
        k = 0
        result = 0 # 1:success / 0:collision

        # 1-Persistent
        # Sensing line (0:idle / 1:busy)
        sensing = random.randrange(0,2)

        while (k < self.Kmax):
            print("k:", k)
            print("Sensing line for idle.")

            # If the line is busy, sensing until the line is idle.
            while (sensing != 0):
                sensing = random.randrange(0,2)

            print("Node start transmit.")

            # Check for collision.
            t_end = time.time()+self.Tfr
            while time.time()<t_end:
                result = random.randrange(0, 2)
                if result == 0:
                    break

            if result == 1:
                return 1   # success

            # retry
            print("Send jamming signal.")
            k += 1
            r = random.randrange(0, 2 ** k)
            Tb = r * self.Tfr
            print("R:", r)
            print("Tb:", Tb)
            print("Wait Tb time.\n")

        return 0   # fail


if __name__ == "__main__":
    mac = Mac()
    result = mac.CSMACD()
    if result == 1:
        print("Transmission success.")
    else:
        print("Transmission fail.")