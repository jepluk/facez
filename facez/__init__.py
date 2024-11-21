import requests
import sqlite

class Main:
    def __init__(self, cookie: str) -> None:
        self.ses = requests.session()
        self.cookie = cookie

    def scrape_token(self) -> tuple:        
        get = self.ses.get(
            'https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/',
            headers={
                'Accept-Language': 'id,en;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                'Referer': 'https://www.instagram.com/',
                'Host': 'www.facebook.com',
                'Sec-Fetch-Mode': 'cors',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Dest': 'empty',
                'Origin': 'https://www.instagram.com',
                'Accept-Encoding': 'gzip, deflate',
            },
            cookies={'cookie': self.cookie}
        )

        print(get.headers)
        if '"access_token":' in str(get.headers):
            print('xxx')
        else: 
            print('no')
