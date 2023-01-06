import json
import os
import platform
import time

import cpuinfo
import psutil
import speedtest
from vkbottle.bot import BotLabeler, Message

import config

bl = BotLabeler()
bl.vbml_ignore_case = True




@bl.message(text=["путь", "Путь"])
async def greeting(message: Message):
    admin = json.load(open(config.faile))
    if not message.from_id == admin['sozd']:
        return
    else:
        text = f'Текущая рабочая директория: {os.getcwd()}'

        return text


async def cm(cmd):

    try:
        os.system(cmd)
        return "OK"
    except:
        return "ERROR"


@bl.message(text=["команда <cmd>", "Команда <cmd>"])
async def greetng(message: Message, cmd: str):
    admin = json.load(open(config.faile))
    if not message.from_id == admin['sozd']:
        return
    else:
        return str(await cm(cmd=cmd))


@bl.message(text=["открыть <cmd>"])
async def greetng(message: Message, cmd: str):
    admin = json.load(open(config.faile))
    if not message.from_id == admin['sozd']:
        return
    else:
        handle = open(cmd, "r")
        data = handle.read()
        return str(data)


@bl.message(text=["cd <cmd>", "Cd <cmd>"])
async def grzeeting(message: Message, cmd: str):
    admin = json.load(open(config.faile))
    if not message.from_id == admin['sozd']:
        return

    else:
        os.chdir(cmd)

        return "Теперь ты " + str(cmd)


@bl.message(text=["файлы", "Файлы"])
async def greeewting(message: Message):
    admin = json.load(open(config.faile))
    if not message.from_id == admin['sozd']:
        return
    else:
        lyl = os.getcwd()
        sees = ""
        see = os.listdir(path=str(lyl))
        i = 0
        for se in see:
            i += 1
            sees += f'{i}. ' + se + '\n'
        text = "Вот тут что тут есть" + '\n' + '\n' + sees
        return text


@bl.message(text=["Сервер", "сервер"])
async def grpoeeting(message: Message):

    admin = json.load(open(config.faile))
    if not message.from_id == admin['sozd']:
        return
    else:
        lll = psutil.virtual_memory().total

        test = speedtest.Speedtest()
        download1 = test.download()
        upload1 = test.upload()
        download = round(download1 / 1024) / 1024
        upload = round(upload1 / 1024) / 1024
        kek = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').total
        dis = psutil.disk_usage("/").used
        di = round(disk) / 1000000000
        lil = round(lll) / 1000000000
        diss = round(dis) / 1000000000
        sett = psutil.net_io_counters().bytes_sent
        settt = round(sett) / 1000000
        sett_p = psutil.net_io_counters().bytes_recv
        settt_p = round(sett_p) / 1000000
        text = f'''
Информация о процессоре: {platform.processor()}, {cpuinfo.get_cpu_info()['brand_raw']}

Система {platform.platform()}

Speed: {round(download)} Mb/s 

Upload Speed : {round(upload)} Mb/s

Версия python: {cpuinfo.get_cpu_info()["python_version"]}

Количество ядер: {psutil.cpu_count(logical=False)}

CPU: {psutil.cpu_percent(interval=1)}%

RAM {kek} %

Всего RAM: {round(lil)} ГБ

Места на диске: {round(di)} ГБ

Занято места: {round(diss)} ГБ

Количество отправленных МБ: {round(settt)}

Количество принятых МБ: {round(settt_p)}

Собрал ответ за  {round(time.time() - message.date, 2)} секунд
            '''

        return text
