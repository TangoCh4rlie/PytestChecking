from digger import *
import time

class Test:
    number1 = 2
    number2 = 12

    def test_add(self):
        num = add(self.number1,self.number2)
        assert(num == 14)
        print("test 1 passed")

    def test_sub(self):
        num = sub(self.number1,self.number2)
        assert(num == -10)
        print("test 2 passed")

    def test_multiply(self):
        num = multiply(self.number1,self.number2)
        assert(num == 24)
        print("test 3 passed")


test = Test()
test.test_add()
time.sleep(1)
test.test_sub()
time.sleep(1)
test.test_multiply()