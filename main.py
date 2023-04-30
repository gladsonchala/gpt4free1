import telebot
import gpt4free
from gpt4free import forefront

# Create a new Telegram bot
bot = telebot.TeleBot("5879800806:AAF61W_F76vbTR3SFa6_59syolJUPgf6Rhg")

# Welcome message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the OMGbot! Send a message to get description on the topic of your choice.")

# Handle user input text
@bot.message_handler(func=lambda message: True)
def generate_poem(message):
    prompt = message.text
    response = gpt4free.Completion.create(Provider.ForeFront, prompt=prompt, model='gpt-4')
    bot.reply_to(message, response.choices[0].text)


# Start the bot
bot.polling()
