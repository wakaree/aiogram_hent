import logging
from typing import Any, Union

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import MessageEntityType
from aiogram.filters import Command
from aiogram.types import Message, MessageEntity
from pyrogram import Client

BOT_TOKEN = "42:ABC"
router = Router(name=__name__)


def mention_filter(message: Message) -> Union[bool, dict[str, Any]]:
    """
    Use this filter to extract the first mention entity from message.
    :return: A dictionary that'll update handling context.
     Read more: https://docs.aiogram.dev/en/latest/dispatcher/dependency_injection.html
    """
    for entity in message.entities:
        if entity.type == MessageEntityType.MENTION:
            return {"mention": entity}
    return False


async def startup(client: Client) -> None:
    await client.start()


async def shutdown(client: Client) -> None:
    await client.stop()


@router.message(Command("id"), mention_filter)
async def get_id(message: Message, mention: MessageEntity, client: Client) -> Any:
    username = mention.extract_from(message.text)
    user = await client.get_users(username)
    return message.answer("ID: {user.id}".format(user=user))


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    client = Client(
        name="bot",
        bot_token=BOT_TOKEN,
        api_id=12345678,
        api_hash="abcdefghj123456",
        no_updates=True,  # We don't need to handle incoming updates by client
    )

    dp = Dispatcher()
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    return dp.run_polling(bot, client=client)


if __name__ == "__main__":
    main()
