import unittest
import main

class MyTestClass(unittest.TestCase):
    def test_sumNum(self):
        num = main.Number(1, 2, 3, 4, 5)
        result = num.sumNum()
        self.assertEqual(14, result)

    def test_sumNum(self):
        num2 = main.Number(11, 22, 32, 43, 55)
        result = num2.sumNum()
        self.assertEqual(163, result)