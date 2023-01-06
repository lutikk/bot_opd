
from vkbottle.bot import BotLabeler
from vkbottle.bot import Message

from utils import search_user_ids, get_forward
import requests as req

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=[
    'группы',
    "группы <url>"
])
async def greetin(message: Message, url: str = ''):
    user_id = await search_user_ids(message)
    if len(user_id) == 0:
        us = message.from_id
    else:
        us = user_id[0]


    ss = req.post('https://luxuryduty.ru/api/dutys/get_grp/', json={'id': us})

    lol = ss.json()
    print(lol)
    text = lol['response']['text']
    return text
