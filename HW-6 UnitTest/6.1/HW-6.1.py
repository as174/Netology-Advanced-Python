# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 21:13:47 2019

@author: AS
"""
#
#Следует протестировать основные функции 
#по получению информации о документах, добавлении и удалении элементов из словаря.
#Используйте fixture для загрузки данных в тестовый класс

import unittest
import json
import secretary
from mock import patch

documents = []
directories = {}
def setUpModule():
    with open('fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))

@patch('secretary.documents', documents, create=True)
@patch('secretary.directories', directories, create=True)

class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
      self.example_set = {
        'shelf_number': 33,
        'doc_number': 22,
        'doc_type': 'test_doc',
        'doc_owner_name': 'test testovich'
      }

    def test_get_all_doc_owners_names(self): 
        self.assertGreater(len(get_all_doc_owners_names()), 0)
     
    
    def test_append_doc_to_shelf(self):
        secretary.append_doc_to_shelf(self.example_set['doc_number'], self.example_set['shelf_number'])
        self.assertIn(self.example_set['doc_number'], directories.get(self.example_set['shelf_number']))


    def test_delete_doc(self):
      self.assertTrue(check_document_existance("10006")) 
      with patch('secretary.input', return_value="10006") as test_doc:
        delete_doc()
      self.assertFalse(check_document_existance("10006")) 



if __name__ == '__main__':
    unittest.main()
