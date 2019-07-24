import unittest
import draft2

class TestDraft(unittest.TestCase):
    
    def setUp(self):
        self.user = 1306975
    
    def test_find_user_id(self):
        self.assertGreater((draft2.find_user_id(self.user)), 0)
        print('Есть id')
        

    
if __name__ == '__main__':
    unittest.main()