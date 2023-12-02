class A:
    def __init__(self) -> None:
        self.__a = 1
        self.a_called = 0

    @staticmethod
    def method1(num1, num2):
        return num1 + num2

    @classmethod
    def method2(cls, num1, num2):
        print(cls)
        return num1 + num2

    @property
    def a(self):
        self.a_called += 1
        return self.__a + 1, self.a_called


A.method2(2, 3)

a = A()
print(a.method1(1, 2))
