import ex
import unittest
class Testmyf(unittest.TestCase):
    def test_num0(self):
        self.assertEqual(ex.myf(12,2),6.0)
    def test_num1(self):
        self.assertRaises(ZeroDivisionError,ex.myf,12,0)
    def test_num2(self):
        self.assertRaises(ValueError,ex.myf,"a","b")
        
if __name__=="__main__":
    unittest.main()
        