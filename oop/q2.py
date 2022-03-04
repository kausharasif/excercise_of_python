class ByteConverter:
    def __init__(self,bytes):
        self.bytes = bytes
    def getKb(self):
        temp = self.bytes // 1024
        return temp
    def getmb(self):
        temp = self.getKb() // 1024
        return temp
    def getgb(self):
        temp = self.getmb() // 1024
        return temp
    def gettb(self):
        temp = self.getgb() // 1024
        return temp

bytedata = int(input("enter bytes"))
byte = ByteConverter(bytedata)
print("Kb is",byte.getKb())
print("mb is",byte.getmb())
print("gb is",byte.getgb())
print("tb is",byte.gettb())