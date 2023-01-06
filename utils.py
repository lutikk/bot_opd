import json
import re
import vk_api
import config
from typing import TypeVar, Union, Iterable

from vkbottle.bot import Message


T = TypeVar("T")


def get_forward(m: Message) -> dict:
    return json.dumps(dict(
        peer_id=m.peer_id,
        conversation_message_ids=m.conversation_message_id,
        is_reply=True
    ), ensure_ascii=False)


def join(data: Union[str, Iterable], separator: str = ",") -> str:

    if isinstance(data, str):
        data = [data]
    if not data:
        return ''
    return separator.join([str(obj) for obj in data])


async def resolve_url(e: Message, url):
    screen_name = url.split('/')[-1]
    id_ = await e.ctx_api.utils.resolve_screen_name(screen_name)
    print(id_.object_id)
    if id_.object_id:
        return id_.object_id
    else:
        url1 = re.sub('[@*]', '', url)
        print(url1)
        us_id = re.sub('\D', '', url1)
        print(us_id)
        return us_id


def get_or_none(value: T) -> Union[T, str]:
    if value is None:
        return "N/A"
    return value


def b2s(value: bool) -> str:
    if value is None:
        return "N/A"
    return "✅" if value else "🚫"


async def get_user_id_by_domain(user_domain: str):
    """Поиск ID по домену"""
    vk = vk_api.VkApi(token=config.main_token)

    obj = vk.method('utils.resolveScreenName', {"screen_name": user_domain})

    if isinstance(obj, list):
        return
    if obj['type'] == 'user':
        return obj["object_id"]


async def search_user_ids(e: Message):
    result = []

    regex = r"(?:vk\.com\/(?P<user>[\w\.]+))|(?:\[id(?P<user_id>[\d]+)\|)"

    for user_domain, user_id in re.findall(regex, e.text):
        if user_domain:
            result.append(await get_user_id_by_domain(user_domain))
        if user_id:
            result.append(int(user_id))
    if e.reply_message and e.reply_message.from_id > 0:
        result.append(e.reply_message.from_id)

    if e.fwd_messages:
        for msg in e.fwd_messages:
            if msg.from_id > 0:
                result.append(msg.from_id)

    _result = []
    for r in result:
        if r is not None:
            _result.append(r)
    return _result


