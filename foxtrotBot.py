import telebot
from telebot import types
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcomeMessage(message):
    bot.send_message(message.chat.id, 'Привет, я помощник интернет-магазина "Фокстрот". Для более детальной информации напишите пожалуйста в чат команду \n /help.')

bot.polling()