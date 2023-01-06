import json

from dev_up import DevUpAPI
from vkbottle.bot import BotLabeler, Message

import config
import vk, vk_api
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True




@bl.message(text=["обнови <text:str>", "обнови"])
async def greeting(message: Message, text: str = ''):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    print(message)
    attachments = message.reply_message.attachments if message.reply_message else message.attachments

    if not attachments:
        return "Где вложение еблан?"
    ss = []
    print(attachments)
    for att in attachments:
        if att.photo != None:
            if att.photo.access_key == None:
                ss.append(f'photo{att.photo.owner_id}_{att.photo.id}')
            else:
                ss.append(f'photo{att.photo.owner_id}_{att.photo.id}_{att.photo.access_key}')
        elif att.graffiti != None:
            if att.graffiti.access_key == None:
                ss.append(f'graffiti{att.graffiti.owner_id}_{att.graffiti.id}')
            else:
                ss.append(f'graffiti{att.graffiti.owner_id}_{att.graffiti.id}_{att.graffiti.access_key}')
        elif att.audio_message != None:
            if att.audio_message.access_key == None:
                ss.append(f'audio_message{att.audio_message.owner_id}_{att.audio_message.id}')
            else:
                ss.append(
                    f'audio_message{att.audio_message.owner_id}_{att.audio_message.id}_{att.audio_message.access_key}')
        elif att.video != None:
            if att.video.access_key == None:
                ss.append(f'video{att.video.owner_id}_{att.video.id}')
            else:
                ss.append(f'video{att.video.owner_id}_{att.video.id}_{att.video.access_key}')

        elif att.audio != None:
            if att.audio.access_key == None:
                ss.append(f'audio{att.audio.owner_id}_{att.audio.id}')
            else:
                ss.append(f'audio{att.audio.owner_id}_{att.audio.id}_{att.audio.access_key}')
        elif att.doc != None:
            if att.doc.access_key == None:
                ss.append(f'doc{att.doc.owner_id}_{att.doc.id}')
            else:
                ss.append(f'doc{att.doc.owner_id}_{att.doc.id}_{att.doc.access_key}')
    url = ss[0]
    admin['url'] = url

    with open(config.faile, 'w') as f:
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'  # Уведомляем что все прошло удачно ибо надо

@bl.message(text=["обновить телефон контакта <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    admin['telefon'] = url

    with open(config.faile, 'w') as f:
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'

@bl.message(text=["обновить факс <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    admin['faks'] = url

    with open(config.faile, 'w') as f:
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'

@bl.message(text=["обновить почту контакта <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    admin['mail'] = url

    with open(config.faile, 'w') as f:
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'

@bl.message(text=["обновить сайт <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    admin['sait'] = url

    with open(config.faile, 'w') as f:
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'

@bl.message(text=["обновить адрес <url>"])
async def greeting(message: Message, url: str):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        return
    admin['strid'] = url

    with open(config.faile, 'w') as f:
        f.write(json.dumps(admin, ensure_ascii=False, indent=2))
    return 'OK'


@bl.message(text=["помощь юзер"])
async def greetng(message: Message, ):

    handle = open("commands_user.txt", "r", encoding="utf-8")
    data = handle.read()
    return str(data)


@bl.message(text=["помощь"])
async def greetng(message: Message, ):
    admin = json.load(open(config.faile))
    if not message.from_id in admin['admins']:
        handle = open("commands_user.txt", "r", encoding="utf-8")
        data = handle.read()
        return str(data)
    else:
        handle = open("commands.txt", "r", encoding="utf-8")
        data = handle.read()
        return str(data)


@bl.message(text=["контакты", 'адрес', "связь"])
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Телефон: {faile["telefon"]}\n' \
           f'Факс: {faile["faks"]}\n' \
           f'Почта: {faile["mail"]}\n' \
           f'Адрес: {faile["strid"]}\n' \
           f'Сайт: {faile["sait"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text="сайт")
async def greeting(message: Message):
    faile = json.load(open(config.faile, encoding="utf-8"))
    text = f'Сайт: {faile["sait"]}'
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

# я не хочу об этом говорить...
@bl.message(text="расписание")
async def greeting(message: Message):
    faile = json.load(open(config.faile))
    url = faile['url']  # определяем ссылку

    await message.answer(attachment=[url], disable_mentions=1, forward=get_forward(message))




@bl.message(text=["звонки"])
async def greeting(message: Message):
    await message.answer(attachment="photo-207904771_457239017?api_access_key=fa18d546bf9e1a00aa", disable_mentions=1,
                         forward=get_forward(message))


@bl.message(text=["кто админ"])
async def greeting(message: Message):
    ranks_4 = 'Администраторы нашего бота:\n\n'
    admin = json.load(open(config.faile))
    for user in await message.ctx_api.users.get(user_ids=admin['admins']):

        ranks_4 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"
    await message.answer(message=ranks_4, disable_mentions=1, forward=get_forward(message))
