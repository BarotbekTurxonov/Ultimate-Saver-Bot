from time import sleep
import requests
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
from utils.files.spotify import SearchFromSpotify
from utils.files.download_spotify import DownloadMusic
logging.basicConfig(level=logging.INFO)
import re,json
from .tiktok import TikTokDownlaoder
from tiktok_downloader import snaptik
from .shazam import ShazamIO
import os, requests
from .insta import FastDLAppDownloader
from utils.files.shazam import shazamtop




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
    







async def get_download_url(youtube_url):
    url = f"https://youtube-dl.wave.video/info?url={youtube_url}&type=video"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "identity",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.1.1823015802.1696058101; _fbp=fb.1.1696058105574.480886438; _animatronauth=4929D3571C856CEB7EF70E2A6C2B43299A204712FC8C7130EE5AB9AA4136EDC256E86B8EFB24997186A22CCF6E6D44A23C174D7039547C24; animatron:user:is-anon=true; _ga_TLPKT07NG1=GS1.1.1696058101.1.1.1696059877.59.0.0; _animatron_lang=en; mp_1da7a894c2f0d0952209dbb88ef1ef59_mixpanel=%7B%22distinct_id%22%3A%20%22d0d11765c362b9d882eb3755%22%2C%22%24device_id%22%3A%20%2218ae4f0d58f1fee-09b50859bdb55f-26031e51-144000-18ae4f0d58f1fee%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22Place%22%3A%20%22Editor%22%2C%22Product%22%3A%20%22WAVE%22%2C%22Source%22%3A%20%22Google%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%22d0d11765c362b9d882eb3755%22%2C%22Name%22%3A%20%22Guest%22%2C%22Username%22%3A%20%22Guest-1016940072%22%2C%22STUDIO%20Plan%22%3A%20%22Guest%22%2C%22STUDIO%20Subscription%22%3A%20%22Guest%22%2C%22WAVE%20Plan%22%3A%20%22Guest%22%2C%22WAVE%20Subscription%22%3A%20%22Guest%22%7D",
        "Host": "youtube-dl.wave.video",
        "If-None-Match": "W/\"1f008-8t/dv+HDtjepx/ex/iPJm93FVZY\"",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "Windows",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    }
    payload = {
        "url": youtube_url,
        "type": "video",
    }
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    download_url = data.get('formats', [{}])[0].get('downloadUrl')
    print(download_url)
    return download_url




@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    text = message.text
    if re.search(instagram_regex, text):
        msg_del = await message.reply("⏳")
        app = FastDLAppDownloader()
        vid = app.download_url(text)
        if vid:
            try:
                await msg_del.delete()
                await bot.send_document(message.chat.id, vid, caption="Downloaded via @Ultimatedownbot")
                with open(f"{message.message_id}.mp4", 'wb') as video:
                    rrr = requests.get(vid)
                    video.write(rrr.content)
                input_file = types.InputFile(f"{message.message_id}.mp4")
                shazammusic = await shazamtop(f"{message.message_id}.mp4")
                title = shazammusic['title']
                if title is not None:
                    musics = SearchFromSpotify(track_name=title, limit=5)
                    audio_urls = DownloadMusic(musics)
                inline_kbs = types.InlineKeyboardMarkup()
                os.remove(f"{message.message_id}.mp4")


                    
                
            except Exception as err:
                with open(f"{message.message_id}.mp4", 'wb') as video:
                    rrr = requests.get(vid)
                    video.write(rrr.content)
                input_file = types.InputFile(f"{message.message_id}.mp4")
                await bot.send_document(message.chat.id, document=input_file,caption="Downloaded via @Ultimatedownbot")
                shazammusic = await shazamtop(f"{message.message_id}.mp4")
                title = shazammusic['title']


                os.remove(f"{message.message_id}.mp4")
            
            with open(f"{message.message_id}.mp4", 'wb') as video:
                rrr = requests.get(vid)
                video.write(rrr.content)
            shazammusic = await shazamtop(f"{message.message_id}.mp4")
            title = shazammusic['title']

            os.remove(f"{message.message_id}.mp4")
            



    elif "tiktok.com" in text:
        msg_del = await message.reply("⏳")

        res = snaptik(text)
        video = res[0].download(f"{message.message_id}.mp4")
        input_file = types.InputFile(f"{message.message_id}.mp4")
        await msg_del.delete()
        await bot.send_document(message.chat.id, document=input_file,caption="Downloaded via @Ultimatedownbot")
        os.remove(f"{message.message_id}.mp4")

    elif any(substring in text for substring in ["youtube", "youtu.be"]):
        msg_del = await message.reply("⏳")

        try:
            vid = await get_download_url(text)
            await bot.send_video(chat_id=message.chat.id, video=vid, caption="Downloaded via @UltimateDownbot")
        except Exception as err:
            await message.answer("<b>I'm so sorry😔. I cant send large files. I cant send quality of 480P</b>")
        get = requests.get("https://saver-uz.onrender.com/youtube/download/audio/?url={}".format(text))

        link = get.json()['result']['1']['url']
        await bot.send_audio(chat_id=message.chat.id, audio=link)



