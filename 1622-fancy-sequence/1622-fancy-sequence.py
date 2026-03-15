class Fancy:

    def __init__(self):
        self.list = []
        self.a = 1
        self.b = 0
        self.MOD = 10 ** 9 + 7
    def append(self, val: int) -> None:
        val  = (val - self.b+self.MOD)%self.MOD 
        self.list.append(val * pow(self.a, self.MOD-2,self.MOD)% self.MOD)
    def addAll(self, inc: int) -> None:
        self.b += inc % self.MOD
    def multAll(self, m: int) -> None:
        self.a *= m % self.MOD
        self.b *= m  % self.MOD
    def getIndex(self, idx: int) -> int:
        # print(self.list)
        # print(self.a)
        # print(self.b)
        idx = idx% self.MOD
        if idx>=len(self.list):
            return -1
        return ((self.list[idx] * self.a ) + self.b) % self.MOD
        
