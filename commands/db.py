from models import *
from vkbottle.bot import BotLabeler, Message
import json
from tortoise.exceptions import DoesNotExist
import config

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=['+преподовтель <last_name> <first_name> <patronymic>'])
async def greeting(message: Message, last_name: str,  first_name: str, patronymic: str):

    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    try:
        ss = await Prepods.get(last_name=last_name, first_name=first_name, patronymic=patronymic)
        return "Препод уже есть в бд"
    except DoesNotExist:
        await Prepods.get_or_new_prepod(last_name=last_name, first_name=first_name, patronymic=patronymic)
        return "Создал препода"

@bl.message(text=['гет преподавателя <text>'])
async def greeting(message: Message, text: str):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    lst = text.replace('.', '').split()
    first_name = lst[0]
    try:
        last_name = lst[1]
        try:
            patronymic = lst[2]
            ss = await Prepods.get(first_name=first_name, last_name=last_name, patronymic=patronymic)
            text = f"id = {ss.id}"
            return text
        except:
            ss = await Prepods.get(first_name=first_name, last_name=last_name)
            text = f"id = {ss.id}"
            return text
    except:
        ss = await Prepods.get(first_name=first_name)
        text = f"id = {ss.id}"
        return text

@bl.message(text=['кто ведет <text_2>', 'кто ведёт <text_2>'])
async def greeting(message: Message, text_2: str):
    text = f'Предмет "{text_2}" ведут:\n\n'
    ss = await Predmets.filter(name__startswith=text_2)
    print(ss)

    for sq in ss:

        name = await Prepods.get(id=sq.id_prepods_id)
        text += f'{name.last_name} {name.first_name} {name.patronymic}\n'

    return text

@bl.message(text=['+предмет <name> <namder:int>'])
async def greeting(message: Message, name: str, namder: int):

    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return

    try:
        ss = await Predmets.get(name=name, id_prepods_id=int(namder))
        return "Предмет уже есть в бд"
    except DoesNotExist:
        await Predmets.get_or_new_predmets(name=name, id_prepods_id=int(namder))
        return "Создал предмет"

@bl.message(text=['+кабинет <kab:int> <name:int> <namder:int>'])
async def greeting(message: Message, kab: int, name: int, namder: int):

    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    try:
        ss = await Kabinet.get(namber=kab, id_prepods_id=name, id_predmet_id=namder)
        return "Кабинет уже есть в бд"
    except DoesNotExist:
        await Kabinet.get_or_new_kab(namber=kab, id_prepods_id=name, id_predmet_id=namder)
        return "Создал кабинет"


@bl.message(text=['каб <text_2:int>', 'кабинет <text_2:int>'])
async def greeting(message: Message, text_2: int):
    text = f'В кабинете "{text_2}" ведут:\n\n'
    ss = await Kabinet.filter(namber__startswith=text_2)
    print(ss)

    for sq in ss:
        predmet = await Predmets.get(id=sq.id_predmet_id)
        name = await Prepods.get(id=sq.id_prepods_id)
        text += f'Предмет: {predmet.name}\n' \
                f'Преподаватель: {name.last_name} {name.first_name} {name.patronymic}\n\n'

    return text