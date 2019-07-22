# -*- coding: utf-8 -*-
import vk_requests
import json
import datetime
import time
import pymongo
import random

access_token = '829426c34641e6086b09846e79fc3cf15852aa040cb957143bc0500d47bab237f224934e7ca0bad375133'
api = vk_requests.create_api(service_token=access_token, api_version='5.101')

user_id = 1306975


def get_user_info(user_id):
    user_info = api.users.get(user_ids=user_id, fields = ['sex','bdate','home_town'])
    user_info_dict = {}
    user_info_dict['sex'] = user_info[0]['sex']
    birth_year = user_info[0]['bdate'][4:]
    now = datetime.datetime.now()
    year_now = now.year
    age = int(year_now) - int(birth_year)
    user_info_dict['age'] = age
    user_info_dict['home_town'] = user_info[0]['home_town']
    return(user_info_dict)

def get_10_random_pairs(full_list):
    random_list = random.sample(full_list, 10)
    return random_list

def search_people():
    user_info_dict = get_user_info(user_id)
    age_delta = 0
    search_result = api.users.search(count = 1000, fields = ['id'],\
                                 sex = 1, hometown = user_info_dict['home_town'],\
                                 age_from = user_info_dict['age'] - int(age_delta),\
                                 age_to = user_info_dict['age'] + int(age_delta),\
                                 status = 6)
    search_result_list = []
    for pair in search_result['items']:
        if pair['is_closed'] == False:
            search_result_list.append(pair['id'])
    pairs_list = get_10_random_pairs(search_result_list)
    return(pairs_list)


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

#
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
#        photos_json = json.dumps(profile_dict)
#        print(photos_json)
        mongo_insert(profile_dict)
        time.sleep(0.45)

get_profiles()


