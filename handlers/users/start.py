from time import sleep
#Dasturchi @Mrgayratov kanla @Kingsofpy
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
import logging,re
from aiogram import types
from aiogram.types import CallbackQuery
from .insta import instadownloader, InstaDownloader
from data.config import ADMINS
from filters import IsUser, IsSuperAdmin, IsGuest
from filters.admins import IsAdmin
from keyboards.inline.main_menu_super_admin import main_menu_for_super_admin, main_menu_for_admin
from loader import dp, db, bot
from states.send_chanell import SuperAdminStateChannel
logging.basicConfig(level=logging.INFO)


@dp.message_handler(IsAdmin(), CommandStart(), state="*")
async def bot_start_admin(message: types.Message):
    await message.answer(f"Assalom alaykum Admin, {message.from_user.full_name}!",
                         reply_markup=main_menu_for_admin)

@dp.message_handler(IsSuperAdmin(), CommandStart(), state="*")
async def bot_start_super_admin(message: types.Message):
    await message.answer(f"Assalom alaykum Bosh Admin, {message.from_user.full_name}!",
                         reply_markup=main_menu_for_super_admin)


@dp.message_handler(IsUser(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = message.from_user
    try:
        db.add_user(user_id=user.id,name=user.first_name)
    except:
        pass
    user_id = message.from_user.first_name
    await message.reply(f"<b>👋🏻 Salom {user_id}\n\n– Qo'shimcha Ma'lumotlar Uchun:\nSizga Kerakli Bo'lgan Ma'lumot Kodini Kiriting yoki Bu Botga O'tgan Tugmangizni Qaytadan Bosing.</b>")

instagram_regex = r'(https?:\/\/(?:www\.)?instagram\.com\/[-a-zA-Z0-9@:%._+~#=]*)'
tiktok_regex = r'(https?:\/\/(?:www\.)?tiktok\.com\/@[-a-zA-Z0-9_]+\/video\/\d+)'
youtube_regex = r'(https?:\/\/(?:www\.)?youtube\.com\/watch\?v=[a-zA-Z0-9_-]+)'
    


import re,json
from .tiktok import TikTokDownlaoder
from tiktok_downloader import snaptik
from .shazam import ShazamIO
import os, requests
from utils.files.saveVid import download_video
from .insta import FastDLAppDownloader

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    text = message.text
    if re.search(instagram_regex, text):
        msg_del = await message.reply("⏳")
        app = FastDLAppDownloader()
        vid = app.download_url(text)
        if vid:
            await msg_del.delete()
            await bot.send_document(message.chat.id, vid, caption="Downloaded via @Ultimatedownbot")
            with open(f"{message.message_id}.mp4", 'wb') as video:
                rrr = requests.get(vid)
                video.write(rrr.content)
            input_file = types.InputFile(f"{message.message_id}.mp4")
            await bot.send_document(message.chat.id, document=input_file,caption="Downloaded via @Ultimatedownbot")
            os.remove(f"{message.message_id}.mp4")
            



    elif "tiktok.com" in text:
        msg_del = await message.reply("⏳")

        res = snaptik(text)
        video = res[0].download(f"{message.message_id}.mp4")
        input_file = types.InputFile(f"{message.message_id}.mp4")
        await bot.send_document(message.chat.id, document=input_file,caption="Downloaded via @Ultimatedownbot")
        os.remove(f"{message.message_id}.mp4")
        





