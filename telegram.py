#! /usr/bin/env python
# -*- coding: utf-8 -*-

from functions import is_float, is_int
from functions_shale import draw_shale
from functions_renew import draw_renew
from renew_model import lcoe_wind, lcoe_solar, lcoe_gas, price_kwh_storage, discount_rate_storage, years_storage
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

token = '233453069:AAH3dL4PJK8CJxdMshGTUuZNdsm2RS8oP4I'  # id бота
TelegramBot = telepot.Bot(token)


def on_chat_message(msg):

    global model_choice_store
    content_type, chat_type, chat_id = telepot.glance(msg)

    input_data = msg['text']
    if chat_id in model_choice_store:
        model_choice = model_choice_store[chat_id]
    else:
        model_choice = None

    if input_data == '/start':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=u'Прогноз добычи "сланцевой" нефти', callback_data='shale')],
                                                         [InlineKeyboardButton(text=u'ВИЭ Европы', callback_data='renewables')]])
        TelegramBot.sendMessage(chat_id, u'Выберите модель. Для изменения выбора нажмите /start или другую кнопку', reply_markup=keyboard)

    elif model_choice == 'shale':
        input_data = input_data.split()  # введённый текст переделываем в массив

        if input_data[0][:1] == '/':
            input_data[0] = input_data[0][1:]  # обрезаем слеш

        if is_int(input_data[0]) is True and is_float(input_data[1]) is True:
            input_data = list(map(float, input_data))  # сценарии буровых в float
            input_data[0] = int(input_data[0])  # месяцы в int
            draw_shale(input_data)  # запуск модели с входными параметрами
            time.sleep(1)
            TelegramBot.sendPhoto(chat_id, open('chart_shale.png', 'rb'))  # отправка графика в чат
        else:
            TelegramBot.sendMessage(chat_id, 'Shale oil forecast: Wrong arguments')

    elif model_choice == 'renewables':
        input_data = input_data.split()  # введённый текст переделываем в массив

        if input_data[0][:1] == '/':
            input_data[0] = input_data[0][1:]  # обрезаем слеш

        if is_int(input_data[0]) is True and is_float(input_data[1]) is True and is_float(input_data[2]) is True and is_float(input_data[2]) is True \
           and len(input_data) == 4:
            print 'renew entered'
            input_data = list(map(float, input_data))  # сценарии буровых в float
            month = int(input_data[0] - 1)
            start_date = month * 30.4
            end_date = start_date + 30.4
            wind_multiplier = [input_data[1]]
            solar_multiplier = [input_data[2]]
            capacity_storage = [input_data[3]]
            input_data[0] = int(input_data[0])  # месяцы в int
            draw_renew(1, wind_multiplier, solar_multiplier, capacity_storage, lcoe_wind, lcoe_solar, lcoe_gas,
                       price_kwh_storage, discount_rate_storage, years_storage, start_date, end_date)  # запуск модели с входными параметрами
            time.sleep(1)
            TelegramBot.sendPhoto(chat_id, open('chart_renew.png', 'rb'))  # отправка графика в чат
        else:
            TelegramBot.sendMessage(chat_id, 'Europe renewables: Wrong arguments')


def on_callback_query(msg):
    global model_choice_store

    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    chat_id_parse = msg['message']['chat']['id']
    if query_data == 'shale':
        print 'shale pressed'
        model_choice_store[chat_id_parse] = query_data
        TelegramBot.sendMessage(chat_id_parse, u'''Введите данные для модели добычи "сланцевой" нефти. Например: 12 0.6 1
Где первое число это срок прогноза в месяцах, а остальное это сценарии количества буровых
в виде доли от исторического максимума. В данном примере это 60% и 100%. В публичном чате перед параметрами модели необходимо ставить слеш, например: /12 0.6 1''')
    elif query_data == 'renewables':
        print 'renewables pressed'
        model_choice_store[chat_id_parse] = query_data
        TelegramBot.sendMessage(chat_id_parse, u'''Введите данные для модели возобновляемой энергетики Европы. Например: 5 4.5 6 1000
Где первое число это отображаемый на графике месяц (5 = май), второе число это мультипликатор ветряной энергетики, третье - солнечной,
четвёртое - ёмкость аккумуляторов в ГВт*ч. В публичном чате перед параметрами модели необходимо ставить слеш, например: /5 4.5 6 1000''')
    print model_choice_store

global model_choice_store
model_choice_store = {}
TelegramBot.message_loop({'chat': on_chat_message,
                          'callback_query': on_callback_query})

print ('Listening ...')

while 1:  # Keep the program running.
    time.sleep(10)
