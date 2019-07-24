# -*- coding: utf-8 -*-
import vk_requests
import datetime
import time
import pymongo
import random

access_token = ''
api = vk_requests.create_api(service_token=access_token, api_version='5.101')

#user_id = 1306975
#
#
user = input ('Введите id или имя пользователя')
def find_user_id(user):
    try:
        user_id = int(user)
    except ValueError:
        search_id = api.users.search(q = str(user))
        user_id = search_id['items'][0]['id']
    return(user_id)

def get_user_groups():
    groups = api.groups.get(user_ids=user_id)
    user_groups = groups['items']
    return(user_groups)



def get_user_info():
#    user_id = 1306975
    user_id = find_user_id(user)
    user_info = api.users.get(user_ids=user_id, fields = ['sex','bdate','home_town'])
    user_groups = get_user_groups()
    user_info_dict = {}
    user_info_dict['sex'] = user_info[0]['sex']
    bdate = user_info[0]['bdate']
    if len(bdate) == 10 or len(bdate) == 9 or len(bdate) == 8:
        birth_year = user_info[0]['bdate'][-4:]
        now = datetime.datetime.now()
        year_now = now.year
        age = int(year_now) - int(birth_year)
    else:
        while True:
            try:
                age = int(input('Сколько вам лет?'))
            except ValueError:
                print('И все-таки сколько вам лет?')
                continue
            else:
                break
    user_info_dict['age'] = age
    if 'home_town' in user_info[0]:
        if user_info[0]['home_town'] == '':
            user_info_dict['home_town'] = input('Из какого вы города?')
        else:
            user_info_dict['home_town'] = user_info[0]['home_town']
    else:
        user_info_dict['home_town'] = input('Из какого вы города?')
    user_info_dict['groups'] = user_groups
    return(user_info_dict)



def get_10_random_pairs(full_list):
    random_list = random.sample(full_list, 10)
    return random_list

def search_people():
    user_info_dict = get_user_info()
    age_delta = 0
    if user_info_dict['sex'] == 1:
        searching_sex = 2
    else:
        searching_sex = 1
    search_result = api.users.search(count = 20, fields = ['id'],\
                                 sex = searching_sex, hometown = user_info_dict['home_town'],\
                                 age_from = user_info_dict['age'] - int(age_delta),\
                                 age_to = user_info_dict['age'] + int(age_delta),\
                                 status = 6)
    search_result_list = []
    for pair in search_result['items']:
        if pair['is_closed'] == False:
            search_result_list.append(pair['id'])
    pairs_list = []
    for pair in search_result_list:
        pair_dict = {}
        pair_groups = api.groups.get(user_ids=pair)
        pair_group = pair_groups['items']
        pair_dict['id'] = pair
        pair_dict['groups'] = pair_group
        pairs_list.append(pair_dict)
        time.sleep(0.45)
    for pair in pairs_list:
        counter = 0
        for group in user_info_dict['groups']:
            if group in pair['groups']:
                counter +=1
            pair['rank'] = counter
    pairs_list = sorted(pairs_list, key=lambda x: x['rank'])
    top_pairs = pairs_list[-10:]
    pairs_result = []
    for pair in top_pairs:
        pairs_result.append(pair['id'])
    return(pairs_result)


def get_top3_likes(photo):
    like_list = []
    for p in photo['items']:
        like_list.append((p['likes']['count']))
        like_list = sorted(like_list, key = int, reverse = True)
        top3_like_list = like_list[:3]
        return(top3_like_list)

def mongo_insert(data):
    client = pymongo.MongoClient("mongodb://mongoUser:Mongo123@netology-hw-cluster-shard-00-00-czw7w.mongodb.net:27017,netology-hw-cluster-shard-00-01-czw7w.mongodb.net:27017,netology-hw-cluster-shard-00-02-czw7w.mongodb.net:27017/test?ssl=true&replicaSet=Netology-HW-cluster-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.diploma
    collection = db.accounts
    collection.insert_one(data)
    client.close()


def get_profiles():
    for people in search_people():
        photo = api.photos.get(owner_id = people, album_id = 'profile', extended = 1, count = 5)
        top3_like_list = get_top3_likes(photo)
        top_photo = []
        for p in photo['items']:
            if p['likes']['count'] in top3_like_list:
                top_photo.append(p['sizes'][1]['url'])
        profile = 'https://www.vk.com/id' + str(people)
        top_photo.insert(0, profile)
        keys_list = ['id', 'photo1', 'photo2', 'photo3']
        profile_dict = dict(zip(keys_list, top_photo))
        mongo_insert(profile_dict)
        time.sleep(0.45)

if __name__ == '__main__':
    get_profiles()


