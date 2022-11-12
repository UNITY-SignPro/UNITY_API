import sqlite3
import re

conn = sqlite3.connect('../word.db', check_same_thread=False)

# DB 입력 데이터 전처리
def formmating(word):
    return re.sub(pattern=r'\([^)]*\)', repl='', string=word).strip()
# 데이터 조회
def search_word(word):
    return c.execute(f"SELECT * FROM word WHERE origin = '{word}'").fetchone()

def search_link(word):
    return c.execute(f"SELECT * FROM link WHERE word = '{word}'").fetchone()

# 커서 생성
c = conn.cursor()



# NLP 단어 저장
# 테이블 생성
# c.execute('''CREATE TABLE IF NOT EXISTS word
#             (origin text,
#             rename text)''')
# # 데이터 삽입
# for origin, rename in iter(excel_sheet_1):
#     c.execute("INSERT INTO word VALUES(?,?);", (formmating(origin), formmating(rename)))
# # 데이터 저장
# conn.commit()
#
#
import pandas as pd
import numpy as np
excek_sheet_1 = pd.read_csv('human.csv')
excel_sheet_1=list(np.array(excek_sheet_1.values.tolist()))
# Video Link 저장
# 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS link
            (word text,
            link text)''')
# 데이터 삽입
for word, link in excel_sheet_1:
    c.execute("INSERT INTO link VALUES(?,?);", (formmating(word).split(',')[0], link))
# 데이터 저장
conn.commit()
