import os
import telebot
import requests
import json

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# To get data from API
response_API = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
data = json.loads(response_API.text)
local_new_cases     = str(data['data']['local_new_cases'])
update_date_time    = str(data['data']['update_date_time'])
local_new_cases     = str(data['data']['local_new_cases'])
local_active_cases  = str(data['data']['local_active_cases'])
local_total_cases   = str(data['data']['local_total_cases'])
local_deaths        = str(data['data']['local_deaths'])
local_recovered     = str(data['data']['local_recovered'])
local_total_number_of_individuals_in_hospitals = str(data['data']['local_total_number_of_individuals_in_hospitals'])
global_new_cases    = str(data['data']['global_new_cases'])
global_total_cases  = str(data['data']['global_total_cases'])
local_new_deaths    = str(data['data']['local_new_deaths'])
global_deaths       = str(data['data']['global_deaths'])
global_new_deaths   = str(data['data']['global_deaths'])
global_recovered    = str(data['data']['global_recovered'])

# /covid command menu
covidinfo = f"""
ශ්‍රී ලංකාවේ කොරෝනා තත්වය. 🇱🇰

{update_date_time} ට යාවත්කාලීන කරන ලදී.
නව රෝගීන් ගණන - {local_new_cases}
නව මරණ ගණන - {local_new_deaths}
තහවුරු කරන ලද මුළු රෝගීන් ගණන - {local_total_cases}
තවමත් ප්‍රතිකාර ලබන රෝගීන් ගණන - {local_active_cases}
මේ වන විට සුව වූ කොරෝන රෝගීන් ගණන - {local_recovered}
මුළු මරණ සංඛ්‍යාව - {local_deaths}
"""

# /gcovid command menu
gcovidinfo = f"""
සමස්ත ලෝකයේ කොරෝනා තත්වය. 🌎

{update_date_time} ට යාවත්කාලීන කරන ලදී.
නව රෝගීන් ගණන - {global_new_cases}
නව මරණ ගණන - {global_new_deaths}
තහවුරු කරන ලද මුළු රෝගීන් ගණන - {global_total_cases}
මේ වන විට සුව වූ කොරෝන රෝගීන් ගණන - {global_recovered}
මුළු මරණ සංඛ්‍යාව - {global_deaths}
"""
# /help command menu
help = f"""
භාවිතා කළ හැකි විධාන 📌

 • /start - මාව start කිරීම සදහා.
 • /covid - ශ්‍රී ලංකාවේ නවතම කොරෝනා තොරතුරු සදහා.
 • /gcovid -සමස්ත ලෝකයේ නවතම කොරෝනා තොරතුරු සදහා.
 • /about - මම ගැන දැන ගැනීම සදහා.
"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Channel', url='https://t.me/szbots'),
               telebot.types.InlineKeyboardButton(text='Group', url='https://t.me/slplatform')),
    markup.add(telebot.types.InlineKeyboardButton(text='Get Latest Details', callback_data=1)),
    bot.send_message(message.chat.id, text="Hi, කොරෝනා පිළිබද තොරතුරු ලබා ගැනීම සදහා [මාව](http://t.me/szcovidbot) භාවිතා කරන්න පුළුවන්. භාවිතා කරන ආකාරය දැන ගැනීමට /help භාවිතා කරන්න.",parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=["covid"])
def send_message(message):
    bot.send_message(message.chat.id, covidinfo)

@bot.message_handler(commands=["gcovid"])
def send_message(message):
    bot.send_message(message.chat.id, gcovidinfo)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)
    if call.data == '1':
        answer = covidinfo
    bot.send_message(call.message.chat.id, answer) 

@bot.message_handler(commands=["help"])
def send_message(message):
    bot.send_message(message.chat.id, help)  

@bot.message_handler(commands=["about"])
def send_message(message):
    bot.send_message(message.chat.id, "• මම කොරෝනා තොරතුරු දැන ගැනීම සදහා ටිනුර දිනිත් විසින් සාදන ලද Bot කෙනෙකි. \n• සියලු තොරතුරු [සෞඛ්‍ය ප්‍රවර්ධන කාර්‍යංශයෙන්](https://hpb.health.gov.lk) ලබා ගත් තොරතුරු ය.", parse_mode='Markdown')      
             
        
bot.polling()
