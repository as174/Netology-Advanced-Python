# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:13:47 2019

@author: AS
"""


import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

#поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. 
#В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
#привести все телефоны в формат +7(999)999-99-99. 
#Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
#объединить все дублирующиеся записи о человеке в одну.

# TODO 1: выполните пункты 1-3 ДЗ

pattern = re.compile("(8|\+7)(\s?)(\(?)(\d{3})(\)?)(\s?)(\-?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})(\s*\(*(доб\.\s*\d+)*\)*)")

for contact in contacts_list:
    contact[5] = re.sub(pattern, r"+7(\4)\8-\10-\12 \14", contact[5], )
    if contact[1] == '':
        name_separated = contact[0].split(' ')
        contact[0] = name_separated[0]
        contact[1] = name_separated[1]
        try:
            contact[2] = name_separated[2]
        except IndexError:
            contact[2] = ''
    if contact[2] == '':
        firstname_separated = contact[1].split(' ')
        contact[1] = firstname_separated[0]
        try:
            contact[2] = firstname_separated[1]
        except IndexError:
            contact[2] = ''
            
new_contacts_list = []


for i in range(len(contacts_list)):
    for j in range(i + 1, len(contacts_list)):
        if contacts_list[i][0] == contacts_list[j][0]:
            for l in range(len(contacts_list[i])):
                if contacts_list[i][l] == '':
                    contacts_list[i][l] = contacts_list[j][l]
                if contacts_list[j][l] == '':
                    contacts_list[j][l] = contacts_list[i][l]
            new_contact = contacts_list[i]
        else:
            new_contact = contacts_list[i]
    new_contacts_list.append(new_contact)



unique_contacts_set = set(tuple(x) for x in new_contacts_list) 
unique_contacts_list = [ list(x) for x in unique_contacts_set ] 


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(unique_contacts_list)