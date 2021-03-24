
class myClass:
    someVal = 100

    def func1(self, val):
        self.someVal = val

    def func2(self):
        print(self.someVal)


cl1 = myClass()
cl2 = myClass()
cl1.func1(90)
cl1.func2()
cl2.func2()
