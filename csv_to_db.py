from pathlib import Path
Path('data.db').touch()

import sqlite3

# DICT FOR REFERENCE
# data = {
#     'url':      remove_emoji(URL),
#     'title':    remove_emoji(title),
#     'date':     remove_emoji(date),
#     'time':     remove_emoji(time),
#     'body':     body
# }

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''create table _entries (url text, title text, date text, time text, body text)''')

import pandas as pd
users = pd.read_csv('data.csv')
users.to_sql('_entries', conn, if_exists='append', index=False)
c.execute('''select * from _entries''').fetchall()

print("DONE!")
