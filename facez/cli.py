#!/usr/bin/env python3
import os, sys, argparse
import sqlite3
from . import Start

# path management
DB_DIR = os.path.expanduser('~/.facez')
DB_NAME = os.path.join(DB_DIR, 'database.db')

if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)
    print(DB_DIR)

# connect to sqlite3 database
def connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS user (cookie TEXT NOT NULL, token TEXT)')
        cursor.execute('CREATE TABLE IF NOT EXISTS useragents (ua TEXT)')
        cursor.execute('CREATE TABLE IF NOT EXISTS dump (id TEXT NOT NULL UNIQUE, NAME TEXT)')
        conn.commit()
        
        return conn
    except sqlite3.error:
        print('\n[ OOPS! ] Database connection error.')
        sys.exit()

def useragent(ua: str):
    conn = connection()
    conn.cursor().execute(
        'INSERT INTO useragents (ua) VALUES (?)',
        (ua,)
    )
    conn.commit()
    conn.close()

def cookie(cookie: str):
    conn = connection()
    conn.cursor().execute(
        'INSERT INTO user (cookie) VALUES (?)',
        (cookie,)
    )
    conn.commit()
    conn.close()

def dumpfriends(id: str):
    obx = Start()
    after = obx.dump_friends(id)
    while True:
        try:
            obx.dump_friends(id, after)
        except Exception as e:
            break


def main():
    argo = argparse.ArgumentParser()

    argx = argo.add_subparsers(title='action', dest='action', required=True)

    arg = argx.add_parser(name='set')

    arg.add_argument(
        '-UA',
        '--useragent',
        type=str,
        help='add useragent to the database.'
    )
    arg.add_argument(
        '-C',
        '--cookie',
        type=str,
        help='add cookie to the database for login.'
    )
    arg.add_argument(
        '-DF',
        '--dumpfriends',
        type=str,
        help='dump id & name from friends user. <facez -DF "id">'
    )
    
    parse = arg.parse_args()
    print(parse)
    cookie(cookie=parse.cookie)
    print('\n[ INFO! ] Successful add new cookie.')
    Start()
    
main()
