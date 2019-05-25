
class Receiver:
    receivedArray = []
    receivedData = []

    def __init__(self):
        pass

    def set_sender(self, sender):
        self.sender = sender
        pass

    def receiver_frame(self):
        print (self.receivedData)




        for i in range (0, len(self.receivedData)):
            for j in range (0, len(self.receivedData[i])):
                self.receivedArray.append(self.receivedData[i][j])
        print(self.receivedArray)

