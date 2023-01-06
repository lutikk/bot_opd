import json

from vkbottle.bot import BotLabeler, Message

import config
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=['учебная часть', "где учебная часть", "где учебная часть?"])
async def greeting(message: Message):
    text = config.yt
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["справка об учебе", "где брать справку с места учебы?", "где брать справку с места учебы"])
async def greeting(message: Message):
    text = config.yt
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["где взять допуск", "где взять допуск?", "где брать допуск?", "где брать допуск"])
async def greeting(message: Message):
    text = config.yt
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["что такое допуск?", "что такое допуск"])
async def greeting(message: Message):
    text = config.dopysk
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["печати", "где ставить печати?", "где ставить печати"])
async def greeting(message: Message):
    text = config.pet
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["кто главный?", "кто главный", "босс", "директор"])
async def greeting(message: Message):
    text = config.director
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["кто декан", "кто декан?", "декан"])
async def greeting(message: Message):
    text = config.dekan
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["кто зав учебной частью", "кто зав учебной частью?"])
async def greeting(message: Message):
    text = config.zav_yt
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["потерял пропуск"])
async def greeting(message: Message):
    text = config.popysk
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["печать документов", "где распечатать документы", "где распечатать документы?"])
async def greeting(message: Message):
    text = config.docs_pet
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))



@bl.message(text=["бахилы", "где купить бахилы?", "где купить бахилы", "купить бахилы"])
async def greeting(message: Message):
    text = config.bax
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["интернет", "где воспользоваться интернетом?", "где воспользоваться интернетом",
                  "где найти интернет", "где найти интернет?"])
async def greeting(message: Message):
    text = config.inet
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["педагог организатор", "организатор", "кто педагог организатор?", "кто педагог организатор"])
async def greeting(message: Message):
    text = config.organozatop
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))

@bl.message(text=["курсы", "какие есть курсы", "какие есть курсы", "кружки"])
async def greeting(message: Message):
    text = config.kurs
    await message.answer(message=text , disable_mentions=1, forward=get_forward(message))




