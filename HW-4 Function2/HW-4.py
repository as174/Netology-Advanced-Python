# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:00:40 2019

@author: AS
"""

#Создать приложение телефонная книга. класс Contact имеет следующие поля:
#Имя, фамилия, телефонный номер - обязательные поля;
#избранный контакт - необязательное поле. По умолчанию False;
#Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети)
# - необходимо использовать *args, **kwargs.

class Contact:
        
        def __init__ (self, name, surname, phone, favorites = 'False', **kwargs):
            self.name = name
            self.surname = surname
            self.phone = phone
            self.favorites = favorites
            self.additional_info = kwargs

        def __str__ (self):
            if self.favorites == 'False':
                self.favorites_status = 'нет'
            else:
                self.favorites_status = 'да'
            return f'Имя: {self.name} \n'\
                   f'Фамилия: {self.surname} \n'\
                   f'Телефон: {self.phone} \n'\
                   f'В избранных: {self.favorites_status} \n'\
                   f'Дополнительная информация: \n'\
                   f'{self.additional_info.keys()} : {self.additional_info.values()}'
#                   f'\r {key} : {value} for key, value in self.additional_info.items():'

 

            
jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')


print(jhon)


#for key, value in jhon.additional_info.items():
#    print(key, ':', value)

