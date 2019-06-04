# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:56:53 2019

@author: RU20009341
"""

#Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
#Записывает в файл пару: страна – ссылка.
#
#Написать генератор, который принимает путь к файлу. 
#При каждой итерации возвращает md5 хеш каждой строки файла.

import json

class Country_iterator:
    
    def __init__(self, path):
        self.counter = 0
        with open(path) as file:
            self.data = json.load(file)
            
    def __iter__(self):
        return(self)
        
    def __next__(self):
        if self.counter < len(self.data):
            return self.data[self.counter]['name']['common']
            self.counter += 1
        else:
            raise StopIteration
            
test_iter = Country_iterator('countries.json')
print(next(test_iter))
print(next(test_iter))
print(next(test_iter))
print(next(test_iter))
print(next(test_iter))
