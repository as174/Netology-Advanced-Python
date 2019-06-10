# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:20:51 2019

@author: AS
"""

#Написать декоратор - логгер. 
#Он записывает в файл дату и время вызова функции, имя функции, 
#аргументы, с которыми вызвалась и возвращаемое значение.

import datetime


#def logger(function):
#    def new_function(*args, **kwargs):
#        result = function(*args, *kwargs)
#        time = str(datetime.datetime.today().strftime('%d/%m/%Y - %H:%M:%S'))
#        arguments = str(args)
#        function_name  = function.__name__
#        log = (time, ' ', function_name, ' ', arguments, ' ', str(result), '\n')
#        with open ('logs.txt', 'a', encoding = 'utf-8') as file:
#                file.writelines(log)
#        return result
#    return new_function
        

#Написать декоратора из п.1 но с параметром – пути к логам.
    
def logger_path(path):
    def logger(function):
        def new_function(*args, **kwargs):
            result = function(*args, *kwargs)
            time = str(datetime.datetime.today().strftime('%d/%m/%Y - %H:%M:%S'))
            arguments = str(args)
            function_name  = function.__name__
            log = (time, ' ', function_name, ' ', arguments, ' ', str(result), '\n')
            with open (path, 'a', encoding = 'utf-8') as file:
                    file.writelines(log)
            return result
        return new_function
    return logger
    
@logger_path('logs.txt')
def trip_calculator(days, eur_rate, eur_per_day):
    result = days * eur_rate * eur_per_day
    return result

italy_trip = trip_calculator(14, 72, 35)
print(italy_trip)