import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

from datetime import datetime

from telethon.tl import types
import asyncio

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time

from telethon.tl import types
from telethon.tl.custom import Button
import random
import asyncio

import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
from random import randint
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID","18049084"))
api_hash = os.environ.get("API_HASH","7e74b1e22026fcc291d32b3d431aa21e")
bot_token = os.environ.get("TOKEN","6110153217:AAFKsN-9NVtVtPTsGpIW03iPCNPb8B-Oik0") # Botunuzun Tokenini Girin.
sahib = os.environ.get("sahib", "rahmetiNC") # Sahiplik Hesabin Kullanıcı Adını Girin .
BOT_ID = int(os.environ.get("BOT_ID", "6110153217")) # Botunuzun İd'si ( Tokenin Başındaki Rakamları ) Girin .
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://lexper:ahritv84@cluster0.hmry6dv.mongodb.net/?retryWrites=true&w=majority") # MongoDB veritabanınızın url'si.
BOT_USERNAME = os.environ.get("BOT_USERNAME","AhriTaggerBot") # Botunuzun kullanıcı adı.
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL","-1001910817002")) # Botunuzun eylemleri kaydedeceği kayıt grubunun id'si.
GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "zeusprochecker") # Botunuzdan yasaklanan kullanıcıların itiraz işlemleri için başvuracağı grup, kanal veya kullanıcı. Boş bırakırsanız otomatik olarak OWNER_ID kimliğine yönlendirecektir.
GONDERME_TURU = os.environ.get("GONDERME_TURU", True) # Botunuzun yanıtladığınız mesajı gönderme türü. Eğer direkt iletmek isterseniz False, kopyasını göndermek isterseniz True olarak ayarlayın.
OWNER_ID = int(os.environ.get("OWNER_ID","5944841427")) # Sahip hesabın id'si
LANGAUGE = os.environ.get("LANGAUGE", "TR")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

anlik_calisan = []
gece_tag = []
rxyzdev_tagTot = {}
rxyzdev_initT = {} 
rxyzdev_stopT = {}

ozel_list = [6219267667]
grup_sayi = []
etiketuye = []

# ~~~~~~~~~~~~~~~~~~~~~~~ gece ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

startmesaj = "👋🏻 ᴍᴇʀʜᴀʙᴀ, ʙᴇɴ ᴀʜʀɪ! ʙᴀᴢı ᴋᴜʟʟᴀɴışʟı ᴏ̈ᴢᴇʟʟɪᴋʟᴇʀᴇ sᴀʜɪᴘ ᴛᴇʟᴇɢʀᴀᴍ ᴜ̈ʏᴇ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ʙᴏᴛᴜʏᴜᴍ.\n\n📚 sɪᴢᴇ ʏᴀʀᴅɪᴍᴄɪ ᴏʟᴀʙɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ!" 
noadmin = "Üzgünüm Ama Yönetici Değilsiniz!"
nogroup = "Komutlar Sadece Grublarda Kullanılabilir!"
nomesaj = "Bana Bir Mesaj Verin!"

#######################

@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def tag(event):
  global gece_tag
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("⤇ ᴇꜱᴋɪ ᴍᴇꜱᴀᴊʟᴀʀɪ ɢᴏʀᴇᴍɪʏᴏʀᴜᴍ!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("⤇ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ᴍᴇꜱᴀᴊɪ ʏᴀᴢᴍᴀᴅɪɴ! ")
  else:
    return await event.respond(f"{nomesaj}")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"🔮 Etiketleme İşlemi Başarıyla Başlatıldı!", buttons=(
                      [
                      Button.url('📣ᴋᴀɴᴀʟ📣 ', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        return
      if usrnum == 8:
        await client.send_message(event.chat_id, f"➻ {msg}\n\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅ İşlem Tamamlandı!\n\n👤 Etiketlerin Sayısı : {rxyzdev_tagTot[event.chat_id]}\n🗣 İşlemi Başlatan : {rxyzdev_initT}", buttons=(
                      [
                      Button.url('📣ʀᴇsᴍɪ ᴋᴀɴᴀʟ📣', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        
#################
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("⤇ Komutlar Sadece Gruplarda Ve Kanallarda Kullanılabilir!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⤇ Üzgünüm Ama Yönetici Değilsiniz!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("⤇ Eski Mesajlar için Üyelerden Bahsedemem!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Bana Bir Metin Ver!**")
  else:
    return await event.respond(f"⤇ {nomesaj}")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("🔮 Etiketleme İşlemi Başarıyla Başlatıldı!", buttons=(
                      [
                      Button.url('📣ʀᴇsᴍɪ ᴋᴀɴᴀʟ📣', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
  
    async for usr in client.iter_participants(event.chat_id,filter=ChannelParticipantsAdmins):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
      if event.chat_id not in anlik_calisan:
        await event.respond("⛔ İşlem Başarıyla İptal Edildi!", buttons=(
                      [
                      Button.url('📣ʀᴇsᴍɪ ᴋᴀɴᴀʟ📣', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**📢 {msg}\n\n{usrtxt}**")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅ Etiketleme İşlemi Başarıyla İptal Edildi!", buttons=(
                      [
                      Button.url('💌 ʀᴇsᴍɪ ᴋᴀɴᴀʟ 💌', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)



###################

#etiket işlemini iptal
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")

  global gece_tag
  gece_tag.remove(event.chat_id)

  sender = await event.get_sender()
  rxyzdev_stopT = f"[{sender.first_name}](tg://user?id={sender.id})"      
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"**⛔ İşlem Başarıyla İptal Edildi!\n\n👤 Etiketlerin Sayısı : {rxyzdev_tagTot[event.chat_id]}\n🗣 İptal Eden : {rxyzdev_stopT}**", buttons=(
                      [
                      Button.url('📣ʀᴇsᴍɪ ᴋᴀɴᴀʟ📣', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")

  global gece_tag
  gece_tag.remove(event.chat_id)

  sender = await event.get_sender()
  rxyzdev_stopT = f"[{sender.first_name}](tg://user?id={sender.id})"      
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"⛔ İşlem İptal Edildi .\n\n👤 Etiketlerin Sayısı : {rxyzdev_tagTot[event.chat_id]}\n🗣 İptal Eden : {rxyzdev_stopT}**", buttons=(
                      [
                      Button.url('📣ʀᴇsᴍɪ ᴋᴀɴᴀʟ📣', f'https://t.me/{GROUP_SUPPORT}')
                      ]
                    ),
                    link_preview=False)

  
# Başlanğıc Mesajı
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"**👋🏻 Merhaba**"
     await event.reply(f"{ad} {startmesaj}", buttons=(
                      [Button.url('🎉 ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ 🎉', f'https://t.me/{BOT_USERNAME}?startgroup=a')],
                      [
                      Button.url("📚 ᴋᴏᴍᴜᴛʟᴀʀ", f'https://t.me/{GROUP_SUPPORT}')
                      ],[
                      Button.url('👤 ᴏᴡɴᴇʀ', f'https://t.me/{sahib}')
                      ]
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"Merhaba!{startmesaj}", buttons=( 
                                                    [Button.url('💌 ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ 💌', f'https://t.me/{BOT_USERNAME}?startgroup=a')],
                                                    [
                                                    Button.url("📚 ᴋᴏᴍᴜᴛʟᴀʀ", f'https://t.me/{GROUP_SUPPORT}')
                                                    ],[
                                                    Button.url('👤 ᴏᴡɴᴇʀ', f'https://t.me/{sahib}')
                                                    ]
                                                  ),
                                                  link_preview=False)

# Başlanğıc Button
@client.on(events.NewMessage(pattern="^/help$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"**👋🏻 Merhaba**"
     await event.reply(f"{ad} {startmesaj}", buttons=(
                      [Button.url('💌 ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ 💌', f'https://t.me/{BOT_USERNAME}?startgroup=a')],
                      [
                      Button.url("📚 ᴋᴏᴍᴜᴛʟᴀʀ", f'https://t.me/{GROUP_SUPPORT}')
                      ],[
                      Button.url('👤 ᴏᴡɴᴇʀ', f'https://t.me/{sahib}')
                      ]
                    ),
                    link_preview=False)

#########################

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(
                f'''**📖 Hey , {msg.from_user.mention}\nBeni Gruba Eklediğin İçin Teşekkürler!''', 
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚙️ Daha Fazla Bilgi için!", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )
        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply('📣 𝖡𝗈𝗍𝗎𝗇 𝖲𝖺𝗁𝗂𝖻𝗂 𝖦𝗋𝗎𝖻𝖺 𝖪𝖺𝗍ı𝗅𝖽ı!')


# Eros oku

import random

@client.on(events.NewMessage(pattern="^/eros$"))
async def eros(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir!")
        return

    # Grup veya kanal katılımcılarını al
    users = await client.get_participants(event.chat_id, limit=200)
    
    users_list = []
    for user in users:
        if user.bot or user.deleted:
            continue  # Silinmiş hesapları veya botları atla
        else:
            users_list.append(user)
    count = len(users_list)
    
    # Rastgele iki kullanıcı seç
    first_user = users_list[random.randint(0, count - 1)]
    second_user = users_list[random.randint(0, count - 1)]
    
    # Belirli kullanıcıları kontrol et
    if (first_user.id == 1550788256 or first_user.id == 5576614947
        or second_user.id == 5375589992 or second_user.id == 5576614947):
        # Belirli kullanıcılar eşleştiğinde özel bir yanıt gönder
        await event.respond("**💌 Eros'un oku atıldı.\n• Aşıklar  :\n\n@[kullanici1](tg://user?id=5053767281) ❤️ @[kullanici2](tg://user?id=5533927130)**")
    else:
        # Rastgele seçilen kullanıcıların adlarını veya kullanıcı adlarını gönder
        percentage = random.randint(1, 100)  # Rastgele bir yüzde hesapla
        await event.respond(f"**💌 Eros'un oku atıldı.\n• Aşıklar  :\n\n@{first_user.username} ❣️ @{second_user.username}\n\n📊 Eşleşme Yüzdesi: {percentage}%**")

@client.on(events.NewMessage(pattern='/slap'))
async def slap(event):
    if event.is_private:
        return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user = reply_message.sender
        if user:
            user_name = user.first_name
            slap_phrases = [
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'nin üstüne benzin döktü!",
                f"{user_name}'yi ateşe attı!",
                f"{user_name}'nin üstüne su döktü!",
                f"{user_name}'yi dondurdu!",
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'yi Zencilere Sattı!",
                f"{user_name}'yi Turşu Kavonozuna Soktu!",
                f"{user_name}'nin Üzerine Buz Dolabı Attı!",
                f"{user_name}'nin Kafasını Duvara Sürterek Yaktı!",
                f"{user_name}'yi Ormana Kaçırdı!",
                f"{user_name}'yi Banyoda Sukast Etti!",
            ]
            slap_phrase = random.choice(slap_phrases)
            await event.respond(f"{event.sender.first_name} {slap_phrase}")
        else:
            await event.respond("Üzgünüm, kullanıcıyı bulamıyorum!")
    else:
        await event.respond("Bu komutu kullanabilmek için bir mesaja yanıt vermelisiniz!")


@client.on(events.NewMessage(pattern="^/bots$"))
async def list_bots(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir!")
        return

    # "Bir saniye bekleyin..." mesajını gönder
    message = await event.respond("🔁 Hazırlanıyor...")

    # 3 saniye bekle
    await asyncio.sleep(3)

    # "Bir saniye bekleyin..." mesajını sil
    await message.delete()

    # Grup veya kanal katılımcılarını al
    users = await client.get_participants(event.chat_id, limit=200)

    bot_list = []
    for user in users:
        if user.bot:
            bot_list.append(user)

    # Bot listesini oluştur ve gönder
    if bot_list:
        bot_names = "\n".join([f"➻ @{user.username}" for user in bot_list])
        await event.respond(f"🤖 Gruptaki Botlar Şunlar:\n\n{bot_names}")
    else:
        await event.respond("🤖 Bu Grupta Hiç Bot Bulamadım!")


# Soru listesi (İstediğiniz kadar soru ekleyebilirsiniz)
soru_listesi = [
    "Nerdesin?",
    "Napiyorsun?",
    "Nasılsın?",
    "Bugün hava nasıl?",
    "Son film tavsiyen nedir?",
    "Hafta sonu planın var mı?",
    "Hangi kitabı okuyorsun?",
    "En sevdiğin yemek nedir?",
    "En son seyahat ettiğin yer neresiydi?",
    "Hobilerin nelerdir?",
    "En sevdiğin mevsim nedir?",
    "Hangi sporu seversin?",
    "En son izlediğin konser hangisiydi?",
    "Hayat felsefen nedir?",
    "En sevdiğin tatil yeri neresi?",
    "Son okuduğun kitap neydi?",
    "En sevdiğin dizi/film nedir?",
    "Hafta içi en sevdiğin gün hangisi?",
    "En sevdiğin renk nedir?",
    "En sevdiğin müzik türü nedir?",
    "Gelecekle ilgili bir hayalin var mı?",
    "En sevdiğin çiçek nedir?",
    "Hangi ülkeyi ziyaret etmek istersin?",
    "En sevdiğin spor takımı hangisi?",
    "Hayatta gerçekleştirmek istediğin bir hedefin var mı?",
    "En sevdiğin meyve nedir?",
    "Son kez gittiğin restoran neresiydi?",
    "En son izlediğin TV programı neydi?",
    "En çok korktuğun şey nedir?",
    "En sevdiğin müzik enstrümanı nedir?",
    "En son hangi oyunu oynadın?",
    "En çok takip ettiğin spor dalı hangisi?",
    "Hayatta yapmak istediğin seyahat nedir?",
    "En sevdiğin hayvan nedir?",
    "En son ne zaman güldün?",
    "Hayatındaki en büyük başarı nedir?",
    "Son zamanlarda izlediğin en iyi film nedir?",
    "İlgi alanlarınız nelerdir?",
    "Dünya turu yapma fırsatın olsa, hangi ülkeleri ziyaret ederdin?",
    "En sevdiğin tarihi dönem nedir?",
    "En iyi arkadaşınla yaptığın en eğlenceli şey nedir?",
    "Sana ilham veren kişi kimdir?",
    "Hayatında dönüm noktası niteliğinde bir anı paylaşır mısın?",
    "En sevdiğin kış sporu nedir?",
    "Bir süper gücün olsaydı, ne olmasını isterdin?",
    "En sevdiğin çizgi film karakteri kim?",
    "En sevdiğin sanat eseri nedir?",
    "En son katıldığın etkinlik nedir?",
    "En sevdiğin klasik film hangisi?",
    "Bir gün yapmayı hayal ettiğin şey nedir?",
    "En sevdiğin takım veya takımlar hangileri?",
    "En güzel çocukluk anını paylaşır mısın?",
    "En sevdiğin sezon nedir?",
    "Geçmişteki en büyük ders nedir?",
    "Hayatındaki en büyük hayal nedir?",
    "En sevdiğin restoran nedir?",
    "Hangi tarihi kişiyi tanıma fırsatını isterdin?",
    "En sevdiğin televizyon dizisi hangisi?",
    "En çok gurur duyduğun şey nedir?",
    "En son hangi yemeği yaptın?",
    "En sevdiğin kahve türü nedir?",
    "En son ne zaman seyahat ettin?",
    "Hayatındaki en büyük hayal kırıklığı nedir?",
    "Hangi müziği dinlerken en çok huzur bulursun?",
    "Gelecekte yapmayı düşündüğün tatil nedir?",
    "En sevdiğin tatil anısı nedir?",
    "Son zamanlarda keşfettiğin yeni bir hobi nedir?",
    "En son gittiğin konser veya etkinlik hangisiydi?",
    "En iyi arkadaşının seninle paylaştığı en güzel anı nedir?",
    "Hangi filmi defalarca izledin?",
    "Hayatında değiştirmeyi düşündüğün bir şey var mı?",
    "En sevdiğin çizgi roman karakteri kim?",
    "Hangi sporu yapmayı en çok seversin?",
    "Hayatta yapmak istediğin en cesurca şey nedir?",
    "Hangi ünlüyle tanışma fırsatın olsa, kim olurdu?",
    "Hangi ünlüyle tanışmak en çok heyecanlandırır seni?",
    "En sevdiğin meyve suyu nedir?",
    "En sevdiğin pizza malzemesi nedir?",
    "En iyi tatlı nedir?",
    "Hangi yiyeceği en çok seversin?",
    "Hangi çeşit müziği dinlemeyi en çok seversin?",
    "En sevdiğin meyve nedir?",
    "En sevdiğin spor dalı nedir?",
    "Gelecekte yaşamak istediğin bir yer var mı?",
    "Hangi dil veya enstrümanı öğrenmek isterdin?",
    "En sevdiğin şehir nedir?",
    "En sevdiğin manzara nedir?",
    "En sevdiğin deniz ürünü nedir?",
    "En sevdiğin çikolata çeşidi nedir?",
    "En son kez gittiğin tatil yeri neresiydi?",
    "En çok kullandığın uygulama nedir?",
    "En sevdiğin tatil etkinliği nedir?",
    "En güzel günün hangisiydi?",
    "Hangi tarihi karakterle sohbet etmek isterdin?",
    "En son hangi restoranda yemek yedin?",
    "Hangi yerel yemeği denemek istersin?",
    "En sevdiğin tatil aktivitesi nedir?",
    "Hangi tatil hatıran en özel?",
    "En sevdiğin yiyecek veya içecek nedir?",
    "En sevdiğin kış aktivitesi nedir?",
    "Hangi çiçeği en çok seversin?",
    "En son izlediğin konser hangisiydi?",
    "Hangi hayvanı evcil olarak beslemek istersin?",
    "Hangi dönemde yaşamayı isterdin?",
    "Hangi hobiye sahip olmak isterdin?",
    "En sevdiğin festivale gitmek ister misin?",
    "En sevdiğin dönem filmleri hangileri?",
    "Hangi tarihi olaya tanıklık etmek isterdin?",
    "En sevdiğin çocukluk oyunu nedir?",
    "Hangi sanat eserini incelemek isterdin?",
    "Hangi ülkeyi ziyaret etmek istersin?",
    "En sevdiğin tarih dönemi nedir?",
    "Hangi tarihi figürü tanımak isterdin?",
    "En sevdiğin radyo istasyonu nedir?",
    "Hangi klasik eseri okumak isterdin?",
    "En sevdiğin film yönetmeni kim?",
    "Hangi ünlüyle bir gün geçirmek isterdin?",
    "En iyi arkadaşının seninle paylaştığı en güzel anı nedir?",
    "En sevdiğin seyahat destinasyonu nedir?"
]

@client.on(events.NewMessage(pattern="^/dtag"))
async def tag(event):
    global gece_tag
    rxyzdev_tagTot[event.chat_id] = 0
    if event.is_private:
        return await event.respond(f"{nogroup}")

    admins = []
    async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
        admins.append(admin.id)
    if event.sender_id not in admins:
        return await event.respond(f"{noadmin}")

    anlik_calisan.append(event.chat_id)

    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("🔮 Etiketleme İşlemi Başarıyla Başlatıldı!", buttons=(
        [
            Button.url('📣ᴋᴀɴᴀʟ📣', f'https://t.me/{GROUP_SUPPORT}')
        ]
    ),
        link_preview=False)

    async for usr in client.iter_participants(event.chat_id):
        rxyzdev_tagTot[event.chat_id] += 1
        usrnum += 1

        # Kullanıcıyı etiketle ve rastgele bir soru seç
        random_user = random.choice(usr)
        random_user_name = random_user.first_name
        random_question = random.choice(soru_listesi)

        usrtxt += f"[{random_user_name}](tg://user?id={random_user.id}) , ({random_question})"

        if event.chat_id not in gece_tag:
            return
        if usrnum == 1:  # 8 kullanıcıyı etiketlemek için
            await client.send_message(event.chat_id, f"➻ {usrtxt}")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:
        await event.respond(f"✅ İşlem Tamamlandı!\n\n👤 Etiketlerin Sayısı : {rxyzdev_tagTot[event.chat_id]}\n🗣 İşlemi Başlatan : {rxyzdev_initT}", buttons=(
            [
                Button.url('📣ʀᴇsᴍɪ ᴋᴀɴᴀʟ📣', f'https://t.me/{GROUP_SUPPORT}')
            ]
        ),
            link_preview=False)



################### VERİTABANI VERİ GİRİŞ ÇIKIŞI #########################
class Database: 
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id): # Veritabanına yeni kullanıcı ekler
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            ),
        )

    async def add_user(self, id): # Veritabına yeni kullanıcı eklemek için ön def
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id): # Bir kullanıcının veritabında olup olmadığını kontrol eder.
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self): # Veritabanındaki toplam kullanıcıları sayar.
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self): # Veritabındaki tüm kullanıcıların listesini verir.
        return self.col.find({})

    async def delete_user(self, user_id): # Veritabından bir kullanıcıyı siler.
        await self.col.delete_many({"id": int(user_id)})

    async def ban_user(self, user_id, ban_duration, ban_reason): # Veritabanınızdaki bir kullanıcıyı yasaklılar listesine ekler.
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason,
        )
        await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def remove_ban(self, id): # Veritabanınızdaki yasaklılar listesinde bulunan bir kullanıcın yasağını kaldırır.
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status(self, id): # Bir kullanıcın veritabanınızda yasaklılar listesinde olup olmadığını kontrol eder.
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        user = await self.col.find_one({"id": int(id)})
        return user.get("ban_status", default)

    async def get_all_banned_users(self): # Veritabınızdaki yasaklı kullanıcılar listesini verir.
        return self.col.find({"ban_status.is_banned": True})


db = Database(DATABASE_URL, BOT_USERNAME)
mongo_db_veritabani = MongoClient(DATABASE_URL)
dcmdb = mongo_db_veritabani.handlers



################## KULLANICI KONTROLLERİ #############
async def handle_user_status(bot: Client, cmd: Message): # Kullanıcı kontrolü
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        if cmd.chat.type == "private":
            await db.add_user(chat_id)
            await bot.send_message(LOG_CHANNEL,LAN.BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id))
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]
            await bot.send_message(LOG_CHANNEL,LAN.GRUP_BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id, chat.title, cmd.chat.id, cmd.chat.id, cmd.message_id))

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if GROUP_SUPPORT:
                msj = f"@{GROUP_SUPPORT}"
            else:
                msj = f"[{LAN.SAHIBIME}](tg://user?id={OWNER_ID})"
            if cmd.chat.type == "private":
                await cmd.reply_text(LAN.PRIVATE_BAN.format(msj), quote=True)
            else:
                await cmd.reply_text(LAN.GROUP_BAN.format(msj),quote=True)
                await bot.leave_chat(cmd.chat.id)
            return
    await cmd.continue_propagation()

############### Broadcast araçları ###########
broadcast_ids = {}


async def send_msg(user_id, message): # Mesaj Gönderme
    try:
        if GONDERME_TURU is False:
            await message.forward(chat_id=user_id)
        elif GONDERME_TURU is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id}: {LAN.NOT_ONLINE}\n"
    except UserIsBlocked:
        return 400, f"{user_id}: {LAN.BOT_BLOCKED}\n"
    except PeerIdInvalid:
        return 400, f"{user_id}: {LAN.USER_ID_FALSE}\n"
    except Exception:
        return 500, f"{user_id}: {traceback.format_exc()}\n"

async def main_broadcast_handler(m, db): # Ana Broadcast Mantığı
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=LAN.BROADCAST_STARTED)
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)
    async with aiofiles.open("broadcast-logs-g4rip.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success))
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(text=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    else:
        await m.reply_document(document="broadcast-logs-g4rip.txt", caption=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    os.remove("broadcast-logs-g4rip.txt")



# Genelde müzik botlarının mesaj silme özelliği olur. Bu özelliği ReadMe.md dosyasındaki örnekteki gibi kullanabilirsiniz.
delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool: # Grup için mesaj silme özeliğinin açık olup olmadığını kontrol eder.
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int): # Grup için mesaj silme özeliğini açar.
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int): # Grup için mesaj silme özeliğini kapatır.
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})

################# SAHİP KOMUTLARI #############
# Verileri listeleme komutu
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def botstats(bot: Client, message: Message):
    g4rip = await bot.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await g4rip.edit(text=LAN.STATS.format(BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__), parse_mode="md")



# Botu ilk başlatan kullanıcıların kontrolünü sağlar.
@app.on_message()
async def G4RIP(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)



# Broadcast komutu
@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)



# Bir kullanıcı yasaklama komutu
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
async def ban(c: Client, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        if len(m.command) <= 1:
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 2:
            ban_duration = 9999
            ban_reason = " ".join(m.command[1:])
    else:
        if len(m.command) <= 1:
            return await m.reply(LAN.NEED_USER)
        elif len(m.command) == 2:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 3:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = " ".join(m.command[2:])
    
        if str(user_id).startswith("-"):
            try:    
                ban_log_text = LAN.BANNED_GROUP.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_GROUP.format(ban_reason))
                await c.leave_chat(user_id)
                ban_log_text += LAN.GROUP_BILGILENDIRILDI
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.GRUP_BILGILENDIRILEMEDI.format(traceback.format_exc())
        else:
            try:    
                ban_log_text = LAN.USER_BANNED.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_USER.format(ban_reason))
                ban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.ban_user(user_id, ban_duration, ban_reason)
        await c.send_message(LOG_CHANNEL, ban_log_text)
        await m.reply_text(ban_log_text, quote=True)


# Bir kullanıcın yasağını kaldırmak komutu
@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
async def unban(c: Client, m: Message):
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
        else:
            if len(m.command) <= 1:
                return await m.reply(LAN.NEED_USER)
            else:
                user_id = int(m.command[1])
        unban_log_text = LAN.UNBANNED_USER.format(m.from_user.mention, user_id)
        if not str(user_id).startswith("-"):
            try:
                await c.send_message(user_id, LAN.USER_UNBAN_NOTIFY)
                unban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                unban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.remove_ban(user_id)
        await c.send_message(LOG_CHANNEL, unban_log_text)
        await m.reply_text(unban_log_text, quote=True)



# Yasaklı listesini görme komutu
@app.on_message(filters.command("blocklist") & filters.user(OWNER_ID))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BLOCKS.format(user_id, ban_duration, banned_on, ban_reason)
    reply_text = LAN.TOTAL_BLOCK.format(banned_usr_count, text)
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await m.reply_text(reply_text, True)



############## BELİRLİ GEREKLİ DEF'LER ###########
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"



########### ÇOKLU DİL ##############
class LAN(object):

    if LANGAUGE == "TR":

        BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})**"
        GRUP_BILDIRIM = "**🏷 Kullanıcı : {}\n📮 ID : {}\n🧝🏻‍♂️ Profili : [{}](tg://user?id={})\n💬 Grub : {}\n🌟 Grub ID: {}\n🎲 Mesaj Linki : [Buraya Tıkla](https://t.me/c/{}/{})**"
        SAHIBIME = "sahibime"
        PRIVATE_BAN = "Üzgünüm, yasaklandınız! Bunun bir hata olduğunu düşünyorsanız {} yazın."
        GROUP_BAN = "Üzgünüm, grubunuz karalisteye alındı! Burada daha fazla kalamam. Bunun bir hata olduğunu düşünyorsanız {} yazın.'"
        NOT_ONLINE = "aktif değil"
        BOT_BLOCKED = "botu engellemiş"
        USER_ID_FALSE = "kullanıcı kimliği yanlış"
        BROADCAST_STARTED = "```📤 BroadCast başlatıldı! Bittiği zaman mesaj alacaksınız!"
        BROADCAST_STOPPED = "✅ ```Broadcast başarıyla tamamlandı.``` \n\n**Şu Kadar Sürede Tamamlandı:** `{}` \n\n**Kayıtlı Toplam Kullanıcı:** `{}` \n\n**Toplam Gönderme Denemesi:** `{}` \n\n**Başarıyla Gönderilen:** `{}` \n\n**Toplam Hata:** `{}`"
        STATS_STARTED = "{} **Lütfen bekleyiniz verileri getiriyorum!**"
        STATS = """**@{} Verileri**\n\n**Kullanıcılar;**\n» **Toplam Sohbetler:** `{}`\n» **Toplam Gruplar: `{}`\n» **Toplam PM's: `{}`"""
        BAN_REASON = "Bu sebep yasaklandığınız için @{} tarafından otomatik olarak oluşturulmuştur"
        NEED_USER = "**Lütfen Kullanıcı kimliği verin.**"
        BANNED_GROUP = "🚷 **Yasaklandı!\n\nTarafından:** {}\n**Grup ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_GROUP = "**Üzgünüm grubunuz kara listeye alındı! \n\nSebep:** `{}`\n\n**Daha fazla burada kalamam. Bunun bir hata olduğunu düşünüyorsanız destek grubuna gelin.**"
        GROUP_BILGILENDIRILDI = "\n\n✅ **Grubu bilgilendirdim ve gruptan ayrıldım.**"
        GRUP_BILGILENDIRILEMEDI = "\n\n❌ **Grubu bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        USER_BANNED = "🚷 **Yasaklandı! \n\nTarafından:** {}\n **Kullanıcı ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_USER = "**Üzgünüm kara listeye alındınız! \n\nSebep:** `{}`\n\n**Bundan sonra size hizmet veremeyeceğim.**"
        KULLANICI_BILGILENDIRME = "\n\n✅ Kişiyi bilgilendirdim."
        KULLANICI_BILGILENDIRMEME = "\n\n❌ **Kişiyi bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        UNBANNED_USER = "🆓 **Kullanıcının Yasağı Kaldırıldı !** \nTarafından: {} \n**Kullanıcı ID:**{}"
        USER_UNBAN_NOTIFY = "🎊 Müjde! Yasağınız kaldırıldı!"
        BLOCKS = "🆔 **Kullanıcı ID**: `{}`\n⏱ **Süre**: `{}`\n🗓 **Yasaklanan Tarih**: `{}`\n💬 **Sebep**: `{}`\n\n"
        TOTAL_BLOCK = "🚷 **Toplam Yasaklanan:** `{}`\n\n{}"

        
app.run()
print(" Bot çalışıyor :)")
client.run_until_disconnected()
