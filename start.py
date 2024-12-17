from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from bot import Bot
from config import *
logger = logging.getLogger(__name__)
from script import LazyDeveloperScript as Script
from database.database import present_user , add_user
# use this if u want to enable force sub 👇
# @Bot.on_message(filters.command('start') & filters.private & subscribed)
# by default using this👇 -> force sub is not required !=> for force sub use 👆
@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except Exception as e:
            print(f"Error adding user: {e}")
            pass
    try:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Official Channel', url='https://t.me/venompredictor'),
                    InlineKeyboardButton('📞Support', url='https://telegram.me/nxzxu/9'),
                ],
                [
                    InlineKeyboardButton('❓ Help', url='https://telegram.me/venomhelpline'),
                    InlineKeyboardButton('🔗 Follow', url="https://github.com/LazyDeveloperr")
                ],
                [
                    InlineKeyboardButton('🚀 Get Predictions', callback_data="getpredictionstext"),
                ]
            ]
        )

        await message.reply_text(
            text=Script.START_TEXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )
    except Exception as lazyerror:
        print(lazyerror)



# ////////////////////////// force subscribe ==> added for feature use /////////////////
# @Bot.on_message(filters.command('start') & filters.private)
# async def not_joined(client: Client, message: Message):
#     try:
#         invite_link = await client.create_chat_invite_link(int(FORCE_SUB_CHANNEL), creates_join_request=False)
#         invite_link2 = await client.create_chat_invite_link(int(FORCE_SUB_CHANNEL2), creates_join_request=False)
#     except ChatAdminRequired:
#         logger.error("Hey Sona, Ek dfa check kr lo ki auth Channel mei Add hu ya nhi...!")
#         return
#     buttons = [
#         [
#             InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=invite_link.invite_link),
#             InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=invite_link2.invite_link),
#         ]
#     ]
#     try:
#         buttons.append(
#             [
#                 InlineKeyboardButton(
#                     text='↻ʀᴇʟᴏᴀᴅ',
#                     url=f"https://t.me/{client.username}?start={message.command[1]}"
#                 )
#             ]
#         )
#     except IndexError:
#         pass
#     await message.reply_chat_action(enums.ChatAction.TYPING)
#     await message.reply(
#         text=FORCE_MSG.format(
#             first=message.from_user.first_name,
#             last=message.from_user.last_name,
#             username=None if not message.from_user.username else '@' + message.from_user.username,
#             mention=message.from_user.mention,
#             id=message.from_user.id
#         ),
#         reply_markup=InlineKeyboardMarkup(buttons),
#         quote=True,
#         disable_web_page_preview=True
#     )

