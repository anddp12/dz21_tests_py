# Задание 1
# Создайте класс, содержащий набор целых чисел. 
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса 
# с помощью модульного тестирования(unittest). 

class Number:
    def __init__(self, n1=int, n2=int, n3=int, n4=int, n5=int) -> None:
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5

    def sumNum(self):
        n = (self.n1, self.n2, self.n3, self.n4, self.n5)
        return sum(n)

    def averageNum(self):
        n = (self.n1, self.n2, self.n3, self.n4, self.n5)
        return sum(n)/5

    def maxNum(self):
        return max(self.n1, self.n2, self.n3, self.n4, self.n5)

    def minNum(self):
        return min(self.n1, self.n2, self.n3, self.n4, self.n5)
