from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

# <b>👋 Hᴇʏ, </b>{}\n 

    START_TEXT = """
<b>I'ᴍ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴀs ᴡᴇʟʟ ᴅɪʀᴇᴄᴛ ʟɪɴᴋs ɢᴇɴᴇʀᴀᴛᴏʀ</b> 
<b>ᴡᴏʀᴋɪɴɢ ᴏɴ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ Gʀᴏᴜᴘ.</b>\n
<blockquote><b>Jᴜꜱᴛ Gɪᴠᴇ /Link Cᴏᴍᴍᴀɴᴅ Iɴ Gʀᴏᴜᴘ Bᴏᴛ Wɪʟʟ Gɪᴠᴇ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ ! (Lᴇᴇᴄʜ Sᴜᴘᴘᴏʀᴛ Lɪɴᴋ)</b></blockquote>\n"""

    HELP_TEXT = """
<b>- ᴀᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ᴏɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ</b>
<b>- sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅᴏᴄᴜᴍᴇɴᴛ ᴏʀ ᴍᴇᴅɪᴀ</b>
<b>- ɪ'ʟʟ ᴘʀᴏᴠɪᴅᴇ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ</b>\n
<b>🔞 ᴀᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.</b>"""

    ABOUT_TEXT = """
<b>⚜ ᴍʏ ɴᴀᴍᴇ : {}</b>\n
<b>✦ ᴠᴇʀsɪᴏɴ : {}</b>\n
<b> Uꜱᴇ, Sʜᴀʀᴇ Aɴᴅ Eɴɪᴏʏ Tʜᴇ Bᴏᴛ !</b>
"""

    STREAM_TEXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🖥 Wᴀᴛᴄʜ :</b> <code>{}</code>\n"""

    DS_TEXT = """
<b>{}</b>\n
<b>ꜱɪᴢᴇ :</b> <code>{}</code>\n
<blockquote><code>{}</code></blockquote>\n"""
    
    STREAM_TEXT_X = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n"""


    BAN_TEXT = "__Aʙᴇʏ BSDK !!, Tᴜᴢʜᴇ Bᴀɴ Kɪᴀ Hᴀɪ, Kʏᴜᴋɪ Tᴜ P@ʀɴ Vɪᴅᴇᴏ Bᴏᴛ Mᴀɪ ᴅᴀʟᴀ__\n\n**[Gᴇᴛ Uɴʙᴀɴ Wɪᴛʜ 𝟸𝟶Rꜱ Fɪɴᴇ !](https://t.me/THE_DS_OFFICIAL)**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            # InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            # InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ]]
    )
    # ABOUT_BUTTONS = InlineKeyboardMarkup(
        # [[
            # InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            # InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            # InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        # ]]
    # )
