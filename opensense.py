import os
import json
import requests
import telebot
from telebot import types
import config

path = 'example.json'

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def cmd_start1(message):
    mess = "Привет! Меня зовут Воздухолов!" + "\n" + "Напиши /get_statistics" + " , и получишь статистику по воздуху." + "\n" + "Мой создатель: @NikolayRisky"
    bot.send_message(message.chat.id, mess)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/get_statistics':
        mess = "В каком месте Курахово?"
        keyboard = types.InlineKeyboardMarkup();
        key_yuhniu = types.InlineKeyboardButton(text='KURAHOVO.ONLINE #1 Южный 18', callback_data='yuhniu'); #кнопка «Да»
        keyboard.add(key_yuhniu); #добавляем кнопку в клавиатуру
        key_prokof = types.InlineKeyboardButton(text='KURAHOVO.ONLINE #2 (Проспект Прокофьева)', callback_data='prokof');
        keyboard.add(key_prokof);
        key_dvorec = types.InlineKeyboardButton(text='KURAHOVO.ONLINE #3 (Дворец Культуры)', callback_data='dvorec');
        keyboard.add(key_dvorec);
        bot.send_message(message.from_user.id, text=mess, reply_markup=keyboard) #следующий шаг – функция get_country
    else:
        bot.send_message(message.from_user.id, 'Напиши /get_statistics');

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yuhniu':
        try:
            yuhniu_answer = 'KURAHOVO.ONLINE #1 Южный 18'
            yhnui = requests.get('https://api.opensensemap.org/boxes/5d8f31af5f3de0001ae89f62/sensors')
            f = open(path, "w")
            f.write(yhnui.text)
            f.close()
            with open(path, 'r') as f:
                data = json.load(f)
                os.remove(path)
                for i in data['sensors']:
                    if i['title'] == 'PM10':
                        yuhniu_answer += "PM10: " + str(i["lastMeasurement"]['value']) + ' µg/m³. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'PM2.5':
                        yuhniu_answer += "PM2.5: " + str(i["lastMeasurement"]['value']) + ' µg/m³. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'Temperatur':
                        yuhniu_answer += "Температура: " + str(i["lastMeasurement"]['value']) + ' °C. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'rel. Luftfeuchte':
                        yuhniu_answer += "Относительная влажность: " + str(i["lastMeasurement"]['value']) + ' %. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'Luftdruck':
                        yuhniu_answer += "Давление воздуха: " + str(i["lastMeasurement"]['value']) + ' Pa. Последнее изменение:' + str(i["lastMeasurement"]['createdAt'])
                bot.send_message(call.message.chat.id, yuhniu_answer)
        except:
            eror = 'Что-то пошло не так, попробуйте снова через 10 секунд.'
            bot.send_message(call.message.chat.id, eror)
    elif call.data == 'prokof':
        try:
            yuhniu_answer = 'KURAHOVO.ONLINE #2 (Проспект Прокофьева)'
            prokofeva = requests.get('https://api.opensensemap.org/boxes/5d8f4f945f3de0001af12c46/sensors')
            f = open(path, 'w')
            f.write(prokofeva.text)
            f.close()
            with open(path, 'r') as f:
                data = json.load(f)
                os.remove(path)
                for i in data['sensors']:
                    if i['title'] == 'PM10':
                        yuhniu_answer += "PM10: " + str(i["lastMeasurement"]['value']) + ' µg/m³. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'PM2.5':
                        yuhniu_answer += "PM2.5: " + str(i["lastMeasurement"]['value']) + ' µg/m³. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'Temperatur':
                        yuhniu_answer += "Температура: " + str(i["lastMeasurement"]['value']) + ' °C. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'rel. Luftfeuchte':
                        yuhniu_answer += "Относительная влажность: " + str(i["lastMeasurement"]['value']) + ' %. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'Luftdruck':
                        yuhniu_answer += "Давление воздуха: " + str(i["lastMeasurement"]['value']) + ' Pa. Последнее изменение:' + str(i["lastMeasurement"]['createdAt'])
                bot.send_message(call.message.chat.id, yuhniu_answer)
        except:
            eror = 'Что-то пошло не так, попробуйте снова через 10 секунд.'
            bot.send_message(call.message.chat.id, eror)
    elif call.data == 'dvorec':
        try:
            yuhniu_answer = 'KURAHOVO.ONLINE #3 (Дворец Культуры)'
            dvorec = requests.get('https://api.opensensemap.org/boxes/5d8f55275f3de0001af2ce5b/sensors')
            f = open(path, 'w')
            f.write(dvorec.text)
            f.close()
            with open(path, 'r') as f:
                data = json.load(f)
                os.remove(path)
                for i in data['sensors']:
                    if i['title'] == 'PM10':
                        yuhniu_answer += "PM10: " + str(i["lastMeasurement"]['value']) + ' µg/m³. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'PM2.5':
                        yuhniu_answer += "PM2.5: " + str(i["lastMeasurement"]['value']) + ' µg/m³. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'Temperatur':
                        yuhniu_answer += "Температура: " + str(i["lastMeasurement"]['value']) + ' °C. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'rel. Luftfeuchte':
                        yuhniu_answer += "Относительная влажность: " + str(i["lastMeasurement"]['value']) + ' %. Последнее изменение:' + str(i["lastMeasurement"]['createdAt']) + '\n'
                    if i['title'] == 'Luftdruck':
                        yuhniu_answer += "Давление воздуха: " + str(i["lastMeasurement"]['value']) + ' Pa. Последнее изменение:' + str(i["lastMeasurement"]['createdAt'])
                bot.send_message(call.message.chat.id, yuhniu_answer)
        except:
            eror = 'Что-то пошло не так, попробуйте снова через 10 секунд.'
            bot.send_message(call.message.chat.id, eror) 
    else:
        bot.send_message(call.message.chat.id, "Нажми на нужную тебе кнопку!") 

if __name__ == "__main__":
    bot.polling(none_stop=True)
