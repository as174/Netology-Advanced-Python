import requests


def query_translate(text, language_input, language_output = 'ru'):

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20181203T174752Z.949933b6bd21e319.3735be4a82be1a600f791f625513c1a4ccdb7403'
    
    params = {
        'key': key,
        'lang': language_input + '-' + language_output,
        'text': text,
        }
       
    response = requests.get(url, params=params, timeout=30).json()
    return response
#    print(response)
#    print(response['code'])
    
    
if __name__ == '__main__':
    print(query_translate('hello', 'en'))
    


    
