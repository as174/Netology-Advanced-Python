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
        
        def __init__ (self, name, surname, phone, favorites = 'False', *args, **kwargs):
            self.name = name
            self.surname = surname
            self.phone = phone
            self.favorites = favorites
            self.kwargs = kwargs
            self.args = args

        def __str__ (self):
            if self.favorites == 'False':
                self.favorites_status = 'нет'
            else:
                self.favorites_status = 'да'
            print  (f'Имя: {self.name} \n'\
                   f'Фамилия: {self.surname} \n'\
                   f'Телефон: {self.phone} \n'\
                   f'В избранных: {self.favorites_status} \n'\
                   f'Дополнительная информация:')
            for item in self.args:
                print (f'\t{item}')
            for k, v in self.kwargs.items():
                print (f'\t{k} {v}')
            return ''

            
jhon = Contact('Jhon', 'Smith', '+71234567809', 'test_arg1', 'test_arg2', telegram='@jhony', email='jhony@smith.com')
peter = Contact('Peter', 'Ivanov', '+7112312312309', favorites = 'True', telegram='@petya', email='petr@mail.com')

print(jhon)
print(jhon.args)

class PhoneBook(Contact):
    
    contact_list = []
    
    def __init__(self, phonebook_name):
        super(Contact, self).__init__()
        self.phonebook_name = phonebook_name

    def get_contacts(self):
        for contact in self.contact_list:
            print(contact)
            
    def add_contact(self, contact):
        self.contact_list.append(contact)
        
    def delete_contact_by_phone(self, phone):
        for contact in self.contact_list: 
            if contact.phone == phone:
                self.contact_list.remove(contact)
    
    def search_favorite_contacts(self):
        for contact in self.contact_list:
            if contact.favorites == 'True':
                print(contact)
            
    def search_contact_by_name_surname(self, name, surname):
        for contact in self.contact_list:
            if contact.name == name and contact.surname == surname:
                print(contact)
                



