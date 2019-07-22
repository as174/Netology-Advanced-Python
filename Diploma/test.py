import unittest
from diploma import draft

class TestDraft(unittest.TestCase):
    
    def setUp(self):
        self.user = 1306975
    
    def test_find_user_id(self):
        self.assertGreater(len(find_user_id(self.user)), 0)
        print('Есть id')
        

    
if __name__ == '__main__':
    unittest.main()