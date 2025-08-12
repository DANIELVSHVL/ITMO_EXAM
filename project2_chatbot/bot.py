import telebot

TOKEN = "ВАШ_ТОКЕН_БОТА"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Это тестовый бот.")

bot.polling()