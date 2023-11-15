# Lekcja - 115 Metody klasy
# robie zadanko z ziomeczkiem krok po kroku

class Computer:
    def __init__(self, cpu, ram = 8192, gpu = 'nVidia', price = 3000):
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu # tylko to, bo reszta w nastepnych metodach
        self.price = price

    def setCpu(self, cpu):
        if cpu.lower() == 'amd' or cpu.lower() == 'intel' or cpu.lower() == "arm":
            self.cpu = cpu 
        else:
            self.cpu = 'unknown'
    
    def setRam(self, ram):
        if type(ram) == int and ram >= 4096:
            self.ram = ram
        else:
            self.ram = 8192  

    def displayInfo(self):
        print(self.cpu, self.gpu, self.ram, self.price)
 

computer1 = Computer('intel', 16000, 'nVidia', 2000 )
computer1.displayInfo()

# Lekcja - 115 Metody klasy
# robie zadanko z ziomeczkiem krok po kroku

class Computer:
    def __init__(self, cpu, ram = 8192, gpu = 'nVidia', price = 3000):
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu # tylko to, bo reszta w nastepnych metodach
        self.price = price

    def setCpu(self, cpu):
        if cpu.lower() == 'amd' or cpu.lower() == 'intel' or cpu.lower() == "arm":
            self.cpu = cpu 
        else:
            self.cpu = 'unknown'
    
    def setRam(self, ram):
        if type(ram) == int and ram >= 4096:
            self.ram = ram
        else:
            self.ram = 8192  

    def displayInfo(self):
        print(self.cpu, self.gpu, self.ram, self.price)
 

computer1 = Computer('intel', 16000, 'nVidia', 2000 )
computer1.displayInfo()
computer2 = Computer('amd', 16000, 'nVidia', 2000 )
computer2.displayInfo()
computer3 = Computer('pizda nie procesor', 16000, 'nVidia', 2000 )
computer3.displayInfo()

