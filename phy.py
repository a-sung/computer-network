class PhysicalLayer:
    def __init__(self):
        pass

    def senderMLT3(self, input):
        output = ""
        flag = 0
        if input[0] == "0":
            output += "0"
        else:
            output += "+"
            flag = 1

        # On running
        for i in range(1, len(input)):
            if input[i] == "0":
                output += output[i - 1]
            else:
                if output[i - 1] == "0":
                    if flag == 1:
                        output += "-"
                    else:
                        output += "+"
                        flag = 0
                else:
                    output += "0"
                    if output[i - 1] == "+":
                        flag = 1
                    elif output[i - 1] == "-":
                        flag = 0
        return output
    
    def receiveMLT3(self, input):
        if input[0] == 0:
            output = '0'
        else:
            output = '1'

        for i in range(0, len(input) - 1):
            if input[i] == input[i + 1]:
                output = output + '0'
            else:
                output = output + '1'
        return output


if __name__ == "__main__":
    # Start sending Data
    print("Start Transmission")
    data = input("data: ")


    # bit -> signal
    phy = PhysicalLayer()
    packet = phy.senderMLT3(data)
    print("bit->signal:", packet)


    # Start Receving Signal
    print("Start Receiving")

    # signal -> bit
    packet = phy.receiveMLT3(packet)
    print("signal:->bit", packet)