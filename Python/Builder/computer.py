class Computer:
    def __init__(self, cpu=None, ram=None, storage=None, gpu=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage}, gpu={self.gpu})"


class ComputerBuilder:
    
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
    
    def setCPU(self, cpu):
        self.cpu = cpu
        return self
    
    def setStorage(self, storage):
        self.storage = storage
        return self
    
    def setRam(self, ram):
        self.ram = ram
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage, self.gpu)


pcBuilder = ComputerBuilder().setCPU(2).setRam(12).setStorage(29).build()
print(pcBuilder)

