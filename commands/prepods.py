
from loguru import logger as log

from vkbottle import API

from models import User
import json
from utils import search_user_ids
from vkbottle.bot import BotLabeler, Message
import os
import config
from os.path import join
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True





@bl.message(text=["создать преподавателя <url>"])
async def greeting(message: Message, url:str):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    api = API(token=config.main_token)
    us_id = search_user_ids(url)
    print(us_id[0])
    prebod_db = await User.get_or_new(id=us_id[0])
    if prebod_db.rank >= 1:
        await message.answer("Уже есть доступ преподавателя", disable_mentions=1, forward=get_forward(message))
    else:
        prebod_db.rank = 1
        await prebod_db.save()
        await message.answer("Дал ранг препода", disable_mentions=1, forward=get_forward(message))


@bl.message(text=["кто ты", "кто вы"])
async def greeting(message: Message):
    text = ''
    api = API(token=config.main_token)
    us_id = message.reply_message.from_id
    user_db = await User.get(id=us_id)
    a = await message.get_user(user_ids=us_id)
    name = f'[id{a.id}|{a.first_name} {a.last_name}]'
    text += f'Это {name}\n'
    if user_db.rank >= 1:
        text += "Должность: Преподаватель\n"
        if user_db.time_work == "нет" or user_db.time_work == None:
            text += "Время работы: Неизвестно\n"
        else:
            text += f'Время работы: {user_db.time_work}\n'
        if user_db.tel == 'нет' or user_db.tel == None:
            text += "Телефон: Неизвестно\n"
        else:
            text += f"Телефон: {user_db.tel}\n"
        if user_db.mail == 'нет' or user_db.mail == None:
            text += "Почта: Неизвестно\n"
        else:
            text += f"Почта: {user_db.mail}\n"
        if user_db.predmet == 'нет' or user_db.predmet == None:
            text += "Предмет: Неизвестно\n"
        else:
            text += f"Предмет: {user_db.predmet}\n"
        if user_db.kab == 'нет' or user_db.kab == None:
            text += "Кабинет: Неизвестно\n"
        else:
            text += f"Кабинет: {user_db.kab}\n"
        if user_db.opis == 'нет' or user_db.opis == None:
            pass
        else:
            text += f"О себе: {user_db.opis}\n"
        await message.answer(text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.rank == 0:
        text += "Должность: Cтудент\n"
        if user_db.opis == 'нет' or user_db.opis == None:
            pass
        else:
            text += f"О себе: {user_db.opis}\n"
        if user_db.tel == 'нет' or user_db.tel == None:
            pass
        else:
            text += f"Телефон: {user_db.tel}\n"
        if user_db.mail == 'нет' or user_db.mail == None:
            pass
        else:
            text += f"Почта: {user_db.mail}\n"
        await message.answer(text, disable_mentions=1, forward=get_forward(message))
        return


@bl.message(text=["кто ты <url>", 'кто вы <url>'])
async def greeting(message: Message, url:str):
    text = ''
    api = API(token=config.main_token)
    us_id = search_user_ids(url)
    print(us_id[0])
    user_db = await User.get(id=us_id[0])
    a = await message.get_user(user_ids=us_id[0])
    name = f'[id{a.id}|{a.first_name} {a.last_name}]'
    text += f'Это {name}\n'
    if user_db.rank >= 1:
        text += "Должность: Преподаватель\n"
        if user_db.time_work == "нет" or user_db.time_work == None:
            text += "Время работы: Неизвестно\n"
        else:
            text += f'Время работы: {user_db.time_work}\n'
        if user_db.tel == 'нет' or user_db.tel == None:
            text += "Телефон: Неизвестно\n"
        else:
            text += f"Телефон: {user_db.tel}\n"
        if user_db.mail == 'нет' or user_db.mail == None:
            text += "Почта: Неизвестно\n"
        else:
            text += f"Почта: {user_db.mail}\n"
        if user_db.predmet == 'нет' or user_db.predmet == None:
            text += "Предмет: Неизвестно\n"
        else:
            text += f"Предмет: {user_db.predmet}\n"
        if user_db.kab == 'нет' or user_db.kab == None:
            text += "Кабинет: Неизвестно\n"
        else:
            text += f"Кабинет: {user_db.kab}\n"
        if user_db.opis == 'нет' or user_db.opis == None:
            pass
        else:
            text += f"О себе: {user_db.opis}\n"
        await message.answer(text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.rank == 0:
        text += "Должность: Cтудент\n"
        if user_db.opis == 'нет' or user_db.opis == None:
            pass
        else:
            text += f"О себе: {user_db.opis}\n"
        if user_db.tel == 'нет' or user_db.tel == None:
            pass
        else:
            text += f"Телефон: {user_db.tel}\n"
        if user_db.mail == 'нет' or user_db.mail == None:
            pass
        else:
            text += f"Почта: {user_db.mail}\n"
        await message.answer(text, disable_mentions=1, forward=get_forward(message))
        return




@bl.message(text=["обновить время преподавателя <url> <text>"])
async def greeting(message: Message, url:str, text: str, **kwargs):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    us_id = search_user_ids(url)
    prepod = await User.get(id=us_id[0])
    prepod.time_work = text
    await prepod.save()
    return 'OK'

@bl.message(text=["обновить телефон преподавателя <url> <text>"])
async def greeting(message: Message, url:str, text: str, **kwargs):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    us_id = search_user_ids(url)

    prepod = await User.get(id=us_id[0])

    prepod.tel = text

    await prepod.save()
    return 'OK'


@bl.message(text=["обновить почту преподавателя <url> <text>"])
async def greeting(message: Message, url:str, text: str, **kwargs):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    us_id = search_user_ids(url)
    prepod = await User.get(id=us_id[0])
    prepod.mail = f'{text}'
    await prepod.save()
    return 'OK'

@bl.message(text=["обновить предметы преподавателя <url> <text>"])
async def greeting(message: Message, url: str, text: str, **kwargs):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    us_id = search_user_ids(url)
    prepod = await User.get(id=us_id[0])
    print(us_id)

    prepod.predmet = f'{text}'
    await prepod.save()
    return 'OK'



@bl.message(text=["обновить кабинет преподавателя <url> <text>"])
async def greeting(message: Message, url:str, text: str, **kwargs):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    us_id = search_user_ids(url)
    prepod = await User.get(id=us_id[0])
    prepod.kab = text
    await prepod.save()
    return 'OK'

@bl.message(text=["обновить описание преподавателя <url> <text>"])
async def greeting(message: Message, url:str, text: str, **kwargs):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    us_id = search_user_ids(url)
    prepod = await User.get(id=us_id[0])
    prepod.opis = text
    await prepod.save()
    return 'OK'


@bl.message(text=["о себе <text>"])
async def greeting(message: Message, text: str, **kwargs):

    prepod = await User.get(id=message.from_id)
    prepod.opis = text
    await prepod.save()
    return 'OK'


@bl.message(text=["телефон <text>", "номер <text>"])
async def greeting(message: Message, text: str, **kwargs):
    prepod = await User.get(id=message.from_id)
    prepod.tel = text
    await prepod.save()
    return 'OK'

@bl.message(text=["почта <text>"])
async def greeting(message: Message, text: str, **kwargs):
    prepod = await User.get(id=message.from_id)
    prepod.mail = text
    await prepod.save()
    return 'OK'