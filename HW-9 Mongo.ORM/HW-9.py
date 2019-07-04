import csv
import re
import pymongo
from pprint import pprint



client = pymongo.MongoClient("mongodb://mongoUser:Mongo123@netology-hw-cluster-shard-00-00-czw7w.mongodb.net:27017,netology-hw-cluster-shard-00-01-czw7w.mongodb.net:27017,netology-hw-cluster-shard-00-02-czw7w.mongodb.net:27017/test?ssl=true&replicaSet=Netology-HW-cluster-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='Windows-1251', newline='') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        for row in reader:
            db.artists.insert_one(row)
            
    for doc in db.artists.find().sort('_id'):
        if 'Цена' in doc:
            doc['Цена'] = int(doc['Цена'])
        db.artists.replace_one({'_id': doc['_id']}, doc)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    result = db.artists.find().sort([('Цена', pymongo.ASCENDING)])
    return(list(result))

def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """

    regex = re.compile(name, re.I)
    
    result = db.artists.find( {'Исполнитель': regex} ).sort([('Цена', pymongo.ASCENDING)])
    return(list(result))

if __name__ == '__main__':
    read_data('artists.csv', db)
    sort_by_price = find_cheapest(db)
    pprint(sort_by_price)
    name = find_by_name("t", db)
    pprint(name)