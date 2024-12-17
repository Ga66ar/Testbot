from bot import Bot
from pyrogram.types import Message
from pyrogram import filters, enums
from config import ADMINS, BOT_STATS_TEXT
from datetime import datetime
from helper_func import get_readable_time

# this is extra feature to get bots uptime 🤞
@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))

