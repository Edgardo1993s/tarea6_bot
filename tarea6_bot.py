import os
import telebot

latid="12°02′06"
long="77°01′07"
TOKEN = '1932761931:AAEjbIjhDGndJI8eqylDnnKM7eMhc3-mmoc'

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['pdf'])

def foto(m):
    cid=m.chat.id
    bot.send_document(cid, open('pdf.pdf','rb'))

@bot.message_handler(commands=['localizacion'])

def local(m):
    cid=m.chat.id
    bot.send_location(cid, latid, long )

bot.polling()