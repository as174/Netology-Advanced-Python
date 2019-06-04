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
        self.counter = -1
        with open(path, encoding = 'utf-8') as file:
            self.data = json.load(file)
            
    def __iter__(self):
        return(self)
        
    def __next__(self):
        self.counter +=1
        if self.counter < len(self.data):
            country_name = self.data[self.counter]['name']['common']
            return (country_name + ' - ' + 'https://en.wikipedia.org/wiki/'+country_name)
        else:
            raise StopIteration
            
test_iter = Country_iterator('countries.json')

for country in test_iter:
    with open ('test.csv', 'a', encoding = 'utf-8') as file:
        file.writelines(country + '\n')