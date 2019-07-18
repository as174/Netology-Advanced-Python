# -*- coding: utf-8 -*-
import vk_requests
import json
import datetime

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


def search_people(user_info_dict):
    user_info_dict = get_user_info(user_id)
    age_delta = 2
    search_result = api.users.search(count = 5, fields = ['id'],\
                                 sex = 1, hometown = user_info_dict['home_town'],\
                                 age_from = user_info_dict['age'] - int(age_delta),\
                                 age_to = user_info_dict['age'] + int(age_delta),\
                                 status = 6)
    pairs_list = []
    for pair in search_result['items']:
        pairs_list.append(pair['id'])
    return(pairs_list)


def get_profiles():
    photos = []
    user_info_dict = get_user_info(user_id)
    for people in search_people(user_info_dict):
        photo = api.photos.get(owner_id = people, album_id = 'profile', extended = 1, count = 10)
        like_list = []
        for p in photo['items']:
            like_list.append((p['likes']['count']))
            like_list = sorted(like_list, key = int, reverse = True)
            top3_like_list = like_list[:3]
        top_photo = []
        for p in photo['items']:
            if p['likes']['count'] in top3_like_list:
                top_photo.append(p['sizes'][1]['url'])
        profile = 'https://www.vk.com/' + str(people)
        top_photo.insert(0, profile)
        photos.append(top_photo)    
    return(photos) 
    
print(get_profiles())