class computer:

    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def config(self):
        print(f"{self.cpu}, {self.ram}, {self.hdd}")

com1 = computer("i5", "16gb", "4TB")
com1.config()
