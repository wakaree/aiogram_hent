import logging

from aiogram import Bot, Dispatcher, Router
from pyrogram import Client

BOT_TOKEN = "42:ABC"
router = Router(name=__name__)


async def startup(client: Client) -> None:
    await client.start()


async def shutdown(client: Client) -> None:
    await client.stop()


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

    dp = Dispatcher(client=client)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    return dp.run_polling(bot)


if __name__ == "__main__":
    main()
