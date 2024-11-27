import wikipedia
import re
import db
from aiogram.types import InlineKeyboardButton
db_settings = db.Database_settings('Db_users.db')


def wiki_search_a(q, page_mode):
    wikipedia.set_lang("ru")
    q_result = wikipedia.page(wikipedia.search(q)[0])
    q_answer = re.sub(r'[(].*,}[)]', '', q_result.summary, 15)
    if page_mode == 1:
        q_str = ''
        j = 0
        for i in q_answer.split('.'):
            j += 1
            q_str += i
            if j == 10:
                break
    else:
        q_str = q_answer.split('.')[0]
    return q_str

def wiki_choise(q):
    wikipedia.set_lang("ru")
    wiki_s = wikipedia.search(q)
    b = []
    for i in range(5):
        w = wiki_s[i]
        c = [InlineKeyboardButton(text=w, callback_data=f'{w}')]
        b.append(c)
    return b

