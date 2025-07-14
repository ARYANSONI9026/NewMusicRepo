from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VILLAIN_MUSIC import app
from config import BOT_USERNAME
from VILLAIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗔ɴɪᴍᴀʟ 𝗞ᴏ 𝗝ᴀᴋᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 

✰ || @smartness_to_hai ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/knight_society2"),
          InlineKeyboardButton("ᴀɴɪᴍᴀʟ", url="https://t.me/tabahi_tabahi"),
          ],
               [
                InlineKeyboardButton("ᴀɴɪᴍᴀʟ ꭙ ꜱᴜᴘᴘᴏʀᴛ˼", url=f"https://t.me/iamvillain77"),
],
[
InlineKeyboardButton("ᴍᴀɪɴ ʙᴏᴛ", url=f"https://t.me/Shizuka_Music_X_Bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/t3mcsf.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
