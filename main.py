import phy
import dl

if __name__ == "__main__":
    data = input("data: ")
    print()

    # Start sending Data
    print("==Start Transmission==")

    # DataLink Layer
    # bit stuffing
    dl = dl.DataLinkLayer()
    packet = dl.stuffing(data)
    print("stuffing:", packet)

    # Physical Layer
    # bit -> signal
    phy = phy.PhysicalLayer()
    packet = phy.senderMLT3(packet)
    print("bit->signal:", packet)
    print()

    # Start Receving Signal
    print("==Start Receiving==")

    # Physical Layer
    # signal -> bit
    packet = phy.receiveMLT3(packet)
    print("signal:->bit", packet)

    # DataLink Layer
    # bit unstuffing
    packet = dl.unstuffing(packet)
    print("unstuffing:", packet)

