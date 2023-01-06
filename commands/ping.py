import time
from pyqiwip2p import QiwiP2P
from vkbottle.bot import BotLabeler
from vkbottle.bot import Message
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from utils import get_forward
from config import main_token, QIWI_PRIV_KEY

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=["пинг"])
async def greeting(message: Message):
    delta = round(time.time() - message.date, 2)
    if delta < 0:
        delta = "666"
    return await message.answer(f"Понг\nВыбесил за {delta} секунд", attachment='photo-201566067_457240629',
                                disable_mentions=1, forward=get_forward(message))


@bl.message(text=["ларионов"])
async def greeting(message: Message):
    return 'Мудак'


@bl.message(text=["ссыль"])
async def greeting(message: Message):

    vk = vk_api.VkApi(token=main_token)
    link_chat = vk.method('messages.getInviteLink', {'peer_id': message.peer_id, 'reset': '0'})
    return str(link_chat)





@bl.message(text=["донат <url:int>", "купить <url:int>"])
async def greeting(message: Message, url: int):

    vk = vk_api.VkApi(token=main_token)
    p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY, default_amount=148)
    new_bill = p2p.bill(amount=url, lifetime=120)
    s = (new_bill.pay_url)
    q = vk.method("utils.getShortLink", {"url": s, "private": 0})["short_url"]
    return str(q)
