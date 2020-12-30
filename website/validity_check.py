import requests, json
def validity_check(api_base_url):

    api_url = f'{api_base_url}/validitycheck/'

    response = requests.get(api_url)

    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print('failed')

if __name__=='__main__':
    api_base_url = 'http://127.0.0.1:8000'
    validity_check(api_base_url)