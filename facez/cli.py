#!/usr/bin/env python3
import os, sys, argparse
import sqlite3

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

def main():
    arg = argparse.ArgumentParser()

    arg.add_parse(name='run')

    arg.add_argument(
        '-ua',
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
    
    parse = arg.parse_args()
    print(parse)
    if parse.action == 'run':
        from .facebook import Main
        Main()
    elif parse.useragent:
        useragent(ua=parse.useragent)
        print('\n[ INFO! ] Successful add new useragent.')
    elif parse.cookie:
        cookie(cookie=parse.cookie)
        print('\n[ INFO! ] Successful add new cookie.')

main()
