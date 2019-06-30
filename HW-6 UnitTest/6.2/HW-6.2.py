# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:13:47 2019

@author: AS
"""
#
#Проверим актуальность API Яндекс.Переводчика для потенциального сервиса переводов. 
#Используя библиотеку request 

import unittest

from yandex import translate


class TestYandexTranslate(unittest.TestCase):
    
    def setUp(self):
        self.translate = query_translate('hello', 'en')
    
    def test_response_code_200(self):
        self.assertEqual(self.translate['code'], 200)
        print('Код ответа соответствует 200')
        
    def test_correct_translate(self):
        self.assertEqual(self.translate['text'], ['привет'])
        print('результат перевода правильный - "привет"')
    
    def test_wrong_input_language(self):
        self.translate = query_translate('hello', 'no_lang')
        self.assertNotEqual(self.translate['code'], 200)
        print('Код ответа не 200 при неизвестном языке')
    
if __name__ == '__main__':
    unittest.main()





