from unittest import TestCase
import info

class testinfo(TestCase):
    

    def SetUp(self):
        """Init"""


    def test_not_empty1(self):
        self.assertNotEquals(info.venv(), "")

   
    def test_not_empty2(self):
        self.assertTrue(info.pip_location())


    def tearDown(self):
        """Finish"""

    
