import telebot
import time

TOKEN = "2071466099:AAEipijRyNKqX8992aEJ2rovk9-4s99E8hQ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    print(message.text)


@bot.message_handler(commands=["hello", "hi"])
def hello(message):
    bot.send_message(message.chat.id, "Hello World")


while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
