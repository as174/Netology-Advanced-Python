import unittest
import draft3


class TestDraft(unittest.TestCase):
    
    def setUp(self):
        self.user = 1306975
        self.user_id = 1306975

    def test_find_user_id(self):
        self.assertGreater((draft3.find_user_id(self.user)), 0)
        print('Есть id')
        
    def test_get_user_info(self):
        user_info_dict = draft3.get_user_info()
        self.assertDictEqual(user_info_dict, {'age': 37, \
                                              'groups': [27168444, 15106510, 48940689, 30666517, 142522504],\
                                              'home_town': 'Москва',\
                                              'sex': 2} )
        print('Данные пользователя получены верно')
        
    def test_get_user_groups(self):
        self.assertGreater(len(draft3.get_user_groups(self.user_id)), 0)
        print('Найдены группы пользователя')
    
if __name__ == '__main__':
    unittest.main()