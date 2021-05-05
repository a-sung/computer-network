class DataLinkLayer:
    def __init__(self):
        pass

    def stuffing(self, input):
        output = input.replace('11111', '111110')
        return output

    def unstuffing(self, input):
        output = input.replace('111110', '11111')
        return output

if __name__ == "__main__":
    # Start sending Data
    print("Start Transmission")
    data = input("data: ")

    # bit stuffing
    dl = DataLinkLayer()
    packet = dl.stuffing(data)
    print("stuffing:", packet)


    # Start Receving Signal
    print("Start Receiving")

    # bit unstuffing
    packet = dl.unstuffing(packet)
    print("unstuffing:", packet)