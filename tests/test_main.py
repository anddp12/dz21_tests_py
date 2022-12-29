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
        
    def test_averageNum(self):
        num3 = main.Number(1, 2, 3, 4, 5)
        result = num3.averageNum()
        self.assertEqual(3.0, result)

    def test_averageNum(self):
        num4 = main.Number(11, 22, 32, 43, 55)
        result = num4.averageNum()
        self.assertEqual(32.6, result)
        
    def test_maxNum(self):
        num5 = main.Number(115, 243, 36, 48, 225)
        result = num5.maxNum()
        self.assertEqual(243, result)

    def test_maxNum(self):
        num6 = main.Number(121, 252, 92, 143, 545)
        result = num6.maxNum()
        self.assertEqual(545, result)
        
    def test_minNum(self):
        num7 = main.Number(115, 243, 36, 48, 225)
        result = num7.minNum()
        self.assertEqual(36, result)

    def test_minNum(self):
        num8 = main.Number(121, 252, 92, 143, 545)
        result = num8.minNum()
        self.assertEqual(92, result)