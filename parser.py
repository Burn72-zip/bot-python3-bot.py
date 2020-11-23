import telebot
import parser

#main variables
TOKEN = "1478089962:AAEByuqGuHwvXgO8w3fD0lpJmPPWbhw2U5I"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'что хотел?')
bot.polling()