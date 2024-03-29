# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:28:19 2019

@author: AS
"""

#Создать класс для работы с почтой;
#Создать методы для отправки и получения писем;
#Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
#Переменные должны быть названы по стандарту PEP8;
#Весь остальной код должен соответствовать стандарту PEP8;
#Класс должен инициализироваться в конструкции.
#if __name__ == '__main__'
#Скрипт для работы с почтой.

import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailWorker:
        
    def __init__ (self, login, password, smtp = 'smtp.gmail.com', imap = 'imap.gmail.com'):
        self.login = login
        self.password = password
        self.smtp = smtp
        self.imap = imap
    
 
    def send_message(self, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        if len(recipients) == 1:
            msg['To'] = ''.join(recipients)
        else:    
            msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain', 'utf-8'))
        ms = smtplib.SMTP(self.smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())
        ms.quit()
    
    def receive_message(self, header = None):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(mailbox = 'inbox')
        if header:
            search_header = '(HEADER Subject "{}")'.format(header)
        else:
            search_header = 'ALL'
        result, data = mail.uid('search', None, search_header)
        if data[0]:
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = str(data[0][1])
            email_message = email.message_from_string(raw_email)
            print(email_message)
            mail.logout()
        else:
            print('There are no letters with current header')

if __name__ == '__main__':        
    test = EmailWorker ('asdasdm@gmail.com', 'asdasdasd')
    test.send_message('a@gmail.com', 'test from PY PY', 'test' )
    test.receive_message()

