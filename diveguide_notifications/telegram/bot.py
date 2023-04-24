import telebot
import os

API_TOKEN = os.environ['API_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

bot = telebot.TeleBot(API_TOKEN)


def notify(message, chat_id=CHAT_ID):
    bot.send_message(chat_id, message)


@bot.message_handler(commands=['start', 'chatid'])
def send_chat_id(message):
    bot.reply_to(message, f"ChatID: {message.chat.id}")


bot.infinity_polling()
