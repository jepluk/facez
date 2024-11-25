import requests
import sqlite3, json, sys
from . import config
from .scrape_token import Token
from .obj import DynamicObject

class Start:
    def __init__(self) -> None:
        self.ses = requests.session()
        with sqlite3.connect(config.DB_PATH) as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM user')
            data = cursor.fetchone()

        if data is not None:
            self.ses.cookies['cookie'] = data[0]
            self.token = data[1] if data[1] else Token(session=self.ses).oauth()
            print(self.token)
        else:
            sys.exit('\n[ WARN! ] Please set cookie.\nExample: facez --cookie "cookie string"')

    def dump_friends(self, id: str, after: str=None) -> None:
        api = self.ses.get('https://graph.facebook.com/'+ str(id), params={'access_token': self.token, 'fields': 'name,friends.fields(id, name)' +(f'.after({after})' if after else '')}).json()
        convert = DynamicObject(api)

        if convert.friends.data:
            with sqlite3.connect(config.DB_PATH) as db:
                for i in convert.friends.data:
                    try:
                        db.cursor().execute('INSERT INTO dump (id, name) VALUES (?,?)', (i.id, i.name))
                    except sqlite3.IntegrityError:
                        pass

                db.commit()

        return convert.friends.paging.cursors.after
