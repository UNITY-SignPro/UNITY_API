import sqlite3
import pandas as pd
import numpy as np
import re

conn = sqlite3.connect('../word.db')
# excel_sheet_1 = pd.read_csv('인간.csv')
# excel_sheet_1 = list(np.array(excel_sheet_1.values.tolist()))

# DB 입력 데이터 전처리
def formmating(word):
    return re.sub(pattern=r'\([^)]*\)', repl='', string=word).strip()
# 데이터 조회
def search_word(word):
    return c.execute(f"SELECT * FROM word WHERE origin = '{word}'").fetchone()

# 커서 생성
c = conn.cursor()
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
