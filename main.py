import telebot
import gpt4free
from gpt4free import Provider, quora, forefront

# Create a new Telegram bot
bot = telebot.TeleBot("5879800806:AAF61W_F76vbTR3SFa6_59syolJUPgf6Rhg")

# Welcome message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the GPT-4 Poetry Bot! Send a message to generate a poem on the topic of your choice.")

# Handle user input text
@bot.message_handler(func=lambda message: True)
def generate_poem(message):
    prompt = message.text
    response = gpt4free.Completion.create(Provider.ForeFront, prompt=prompt, model='gpt-4')
    bot.reply_to(message, response.choices[0].text)

# CoCalc command
@bot.message_handler(commands=['cocalc'])
def generate_cocalc_poem(message):
    response = gpt4free.Completion.create(Provider.CoCalc, prompt='Write a poem on Lionel Messi', cookie_input='')
    bot.reply_to(message, response.choices[0].text)

# Theb command
@bot.message_handler(commands=['theb'])
def generate_theb_poem(message):
    response = gpt4free.Completion.create(Provider.Theb, prompt='Write a poem on Lionel Messi')
    bot.reply_to(message, response.choices[0].text)

# Forefront command
@bot.message_handler(commands=['forefront'])
def generate_forefront_poem(message):
    token = forefront.Account.create(logging=False)
    response = gpt4free.Completion.create(Provider.ForeFront, prompt='Write a poem on Lionel Messi', model='gpt-4', token=token)
    bot.reply_to(message, response.choices[0].text)

# Poe command
@bot.message_handler(commands=['Poe'])
def generate_poe_poem(message):
    token = quora.Account.create(logging=False)
    response = gpt4free.Completion.create(Provider.Poe, prompt='Write a poem on Lionel Messi', token=token, model='ChatGPT')
    bot.reply_to(message, response.choices[0].text)

# You command
@bot.message_handler(commands=['You'])
def generate_you_poem(message):
    response = gpt4free.Completion.create(Provider.You, prompt='Write a poem on Lionel Messi')
    bot.reply_to(message, response.choices[0].text)

# Start the bot
bot.polling()
