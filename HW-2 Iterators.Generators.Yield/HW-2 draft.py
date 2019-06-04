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
import wikipedia


#x = wikipedia.page('Aruba')
#print(x.url)
#country_list = []
#
#with open('countries.json', encoding='utf-8') as file:
#    json_data = json.load(file)
#
#i = 0
#while i < len(json_data):
#    country_list.append(json_data[i]['name']['common'])
#    i += 1
#
#for country in country_list:
#    wiki_page = wikipedia.page(country).url
#    print(wiki_page)

#print(country_list)
    
x = wikipedia.page('Georgia', auto_suggest = True)

print(x)