import telebot
import requests

bot = telebot.TeleBot('5630286293:AAFAN4Nia3tK0rBaIFdR8Lauv3iT33laD68')

@bot.message_handler(commands =['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, юнец, хочешь услышать парочку реальных фактов? Тогда пиши /fact и наслаждайся' )
    
@bot.message_handler(commands =['help'])
def start(message):
    bot.send_message(message.chat.id, f'Настоящий мужчина не просит о помощи. Возьми все в свои руки и разберись!!!' )

@bot.message_handler(commands =['fact'])
def start(message):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    b = response.json()
    bot.send_message(message.chat.id, b['value'] )


bot.polling(none_stop=True)