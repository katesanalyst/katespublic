import requests
import json

def main():

    #this is retrive Data from API; which contains entire details about movie; have to be used JSON filters further...

    response = requests.get(f'https://data.justickets.co/datapax/JUSTICKETS.chennai.naai-sekar-returns.v1.json', headers=headers)
    cdax = json.loads(response.text)
    print(cdax['movie']['name'])
    for x in (cdax['sessions']):
        print(x)



if __name__ == '__main__':

    headers = {
        'authority': 'data.justickets.co',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,ta;q=0.8',
        'cache-control': 'no-cache',
        'origin': 'https://www.justickets.in',
        'pragma': 'no-cache',
        'referer': 'https://www.justickets.in/',
        'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.62',
    }

    main()