from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('TOKEN')

# JANGAN LUPA MENGGUNAKAN chat.id sebagai addres mengirim

# MENGIRIM MEDIA MELALUI LINK
@bot.message_handler(commands=['foto'])
async def send_photo(message):
  chat_id = message.chat.id
  url = 'URL GAMBAR'
  await bot.send_photo(chat_id,url) #Menggunakan send_photo
  
@bot.message_handler(ccommands['video'])
async def send_video(message):
  chat_id = message.chat.id
  url = 'URL VIDEO'
  await bot.send_video(chat_id,url) #Menggunakan send_video
  
@bot.message_handler(commands=['audio'])
async def send_audio(message):
  chat_id = message.chat.id
  url = 'URL AUDIO'
  await bot.send_audio(chat_id,url) #Menggunakan send_audio
  
# MENGIRIM MEDIA MELALUI FILE INTERNAL
@bot.message_handler(commands=['foto_internal'])
async def send_photo_internal(message):
  chat_id = message.chat.id
  with open('FILE-FOTO.jpg','rb') as pict:
    await bot.send_photo(chat_id,url) #Menggunakan send_photo

@bot.message_handler(commands=['video_internal'])
async def send_video_internal(message):
  chat_id = message.chat.id
  with open('FILE-VIDEO.mp4','rb') as pict:
    await bot.send_video(chat_id,url) #Menggunakan send_video
    
@bot.message_handler(commands=['audio_internal'])
async def send_audio_internal(message):
  chat_id = message.chat.id
  with open('FILE-AUDIO.mp3','rb') as pict:
    await bot.send_audio(chat_id,url) #Menggunakan send_audio

import asyncio
asyncio.run(bot.polling())