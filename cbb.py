
from pyrogram import __version__
from bot import Bot
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from script import LazyDeveloperScript as Script

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    # this is sample callback query => modify and use it 🤞
    if data == "getpredictionstext":
        try:
            await query.message.edit_text(
                        text = Script.GET_PREDICT_TEXT,
                        disable_web_page_preview = True,
                    )
        except Exception as lazydeveloper:
            print(lazydeveloper)
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
