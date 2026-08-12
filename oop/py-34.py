class computer:

    brand = "HP"

    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def config(self):
        print(f"{self.cpu}, {self.ram}, {self.hdd}")

    @classmethod
    def info(cls):
        return cls.brand

    @staticmethod
    def greet():
        return "Hello, welcome to the computer class!"


com1 = computer("i5", "16gb", "4TB")
com1.config()
print(com1.info())
print(com1.greet())
