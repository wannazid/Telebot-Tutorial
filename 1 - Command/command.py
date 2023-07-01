from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot('TOKEN')

# Command help dan start
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Halo aku Bot Malas.
Saya disini akan membantu kegiatan di internet dengan fitur-fitur saya ini, terimakasih!\
""")

import asyncio
asyncio.run(bot.polling())