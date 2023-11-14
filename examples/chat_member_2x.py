from typing import Any

from aiogram import Bot, Dispatcher
from aiogram.types import AllowedUpdates, ChatMemberUpdated, ChatType, ParseMode
from aiogram.utils import executor
from magic_filter import F

bot = Bot(token="42:ABC", parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


@dp.chat_member_handler(
    ~F.old_chat_member.is_chat_member(),
    F.new_chat_member.is_chat_member(),
    F.chat.type.in_([ChatType.GROUP, ChatType.SUPERGROUP])
    # More about magic filters: https://docs.aiogram.dev/en/dev-3.x/dispatcher/filters/magic_filters.html
)
async def new_chat_member(update: ChatMemberUpdated) -> Any:
    await bot.send_message(
        chat_id=update.chat.id,
        text=f"Hello, {update.from_user.get_mention()}"
    )


@dp.chat_member_handler(
    F.old_chat_member.is_chat_member(),
    ~F.new_chat_member.is_chat_member(),
    F.chat.type.in_([ChatType.GROUP, ChatType.SUPERGROUP])
)
async def left_chat_member(update: ChatMemberUpdated) -> Any:
    await bot.send_message(
        chat_id=update.chat.id,
        text=f"Bye, {update.from_user.get_mention()}!"
    )


if __name__ == "__main__":
    # Here you need to specify all types of updates that the bot should receive.
    # To combine updates use + operator, for example:
    # AllowedUpdates.MESSAGE + Allowedupdates.CALLBACK_QUERY + AllowedUpdates.CHAT_MEMBER
    executor.start_polling(dp, allowed_updates=AllowedUpdates.CHAT_MEMBER)
