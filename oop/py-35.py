class A:

    def f1(self):
        print("f1 work")

    def f2(self):
        print("f2 work")

    def fin(self):
        print("fin work A")

class B():

    def f3(self):
        print("f3 work")

    def f4(self):
        print("f4 work")

    def fin(self):
        print("fin work B")


class C(B):

    def f5(self):
        print("f5 work")

    def f6(self):
        print("f6 work")

class D(B, A):

    def f7(self):
        print("f7 work")

    def f8(self):
        print("f8 work")

obj1 = D()
obj1.f1()
obj1.fin()