import telebot

bot = telebot.TeleBot('1424843613:AAFmIRdpjBErcD14WQ1Qy-oph_tn7F4mYR8')


@bot.message_text(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, "ПРИВЕТ")


bot.polling()
