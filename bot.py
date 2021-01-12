import telebot
from telebot import types
from parsing import main

bot = telebot.TeleBot('1400637163:AAEvORZYS1rfiCH9dr6YoIk4mhgYyjNGwBg')

keyboard = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton('ALL NEWS', callback_data='ALL_NEWS')
keyboard.add(btn1)

back = types.InlineKeyboardMarkup(row_width=2)
b = types.InlineKeyboardButton('Back', callback_data='BACK')
back.add(b)

back1 = types.InlineKeyboardMarkup(row_width=2)
photo1 = types.InlineKeyboardButton('Фото', callback_data='photo1')
link1 = types.InlineKeyboardButton('Ссылка', callback_data='link1')
b1 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back1.add(photo1, link1, b1)

back2 = types.InlineKeyboardMarkup(row_width=2)
link2 = types.InlineKeyboardButton('Ссылка', callback_data='link2')
b2 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back2.add(link2,b2)

back3 = types.InlineKeyboardMarkup(row_width=2)
photo3 = types.InlineKeyboardButton('Фото', callback_data='photo3')
link3 = types.InlineKeyboardButton('Ссылка', callback_data='link3')
b3 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back3.add(photo3, link3, b3)

back4 = types.InlineKeyboardMarkup(row_width=2)
link4 = types.InlineKeyboardButton('Ссылка', callback_data='link4')
b4 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back4.add(link4, b4)

back5 = types.InlineKeyboardMarkup(row_width=2)
photo5 = types.InlineKeyboardButton('Фото', callback_data='photo5')
link5 = types.InlineKeyboardButton('Ссылка', callback_data='link5')
b5 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back5.add(photo5, link5, b5)

back6 = types.InlineKeyboardMarkup(row_width=2)
link6 = types.InlineKeyboardButton('Ссылка', callback_data='link6')
b6 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back6.add(link6, b6)

back7 = types.InlineKeyboardMarkup(row_width=2)
photo7 = types.InlineKeyboardButton('Фото', callback_data='photo7')
link7 = types.InlineKeyboardButton('Ссылка', callback_data='link7')
b7 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back7.add(photo7, link7, b7)

back8 = types.InlineKeyboardMarkup(row_width=2)
link8 = types.InlineKeyboardButton('Ссылка', callback_data='link8')
b8 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back8.add(link8, b8)

back9 = types.InlineKeyboardMarkup(row_width=2)
photo9 = types.InlineKeyboardButton('Фото', callback_data='photo9')
link9 = types.InlineKeyboardButton('Ссылка', callback_data='link9')
b9 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back9.add(photo9, link9, b9)

back10 = types.InlineKeyboardMarkup(row_width=2)
link10 = types.InlineKeyboardButton('Ссылка', callback_data='link10')
b10 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back10.add(link10, b10)

back11 = types.InlineKeyboardMarkup(row_width=2)
photo11 = types.InlineKeyboardButton('Фото', callback_data='photo11')
link11 = types.InlineKeyboardButton('Ссылка', callback_data='link11')
b11 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back11.add(photo11, link11, b11)

back12 = types.InlineKeyboardMarkup(row_width=2)
link12 = types.InlineKeyboardButton('Ссылка', callback_data='link12')
b12 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back12.add(link12, b12)

back13 = types.InlineKeyboardMarkup(row_width=2)
photo13 = types.InlineKeyboardButton('Фото', callback_data='photo13')
link13 = types.InlineKeyboardButton('Ссылка', callback_data='link13')
b13 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back13.add(photo13, link13, b13)

back14 = types.InlineKeyboardMarkup(row_width=2)
link14 = types.InlineKeyboardButton('Ссылка', callback_data='link14')
b14 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back14.add(link14, b14)

back15 = types.InlineKeyboardMarkup(row_width=2)
photo15 = types.InlineKeyboardButton('Фото', callback_data='photo15')
link15 = types.InlineKeyboardButton('Ссылка', callback_data='link15')
b15 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back15.add(photo15, link15, b15)

back16 = types.InlineKeyboardMarkup(row_width=2)
link16 = types.InlineKeyboardButton('Ссылка', callback_data='link16')
b16 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back16.add(link16, b16)

back17 = types.InlineKeyboardMarkup(row_width=2)
photo17 = types.InlineKeyboardButton('Фото', callback_data='photo17')
link17 = types.InlineKeyboardButton('Ссылка', callback_data='link17')
b17 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back17.add(photo17, link17, b17)

back18 = types.InlineKeyboardMarkup(row_width=2)
link18 = types.InlineKeyboardButton('Ссылка', callback_data='link18')
b18 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back18.add(link18, b18)

back19 = types.InlineKeyboardMarkup(row_width=2)
photo19 = types.InlineKeyboardButton('Фото', callback_data='photo19')
link19 = types.InlineKeyboardButton('Ссылка', callback_data='link19')
b19 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back19.add(photo19, link19, b19)

back20 = types.InlineKeyboardMarkup(row_width=2)
link20 = types.InlineKeyboardButton('Ссылка', callback_data='link20')
b20 = types.InlineKeyboardButton('Назад', callback_data='BACK')
back20.add(link20, b20)

pagin = types.InlineKeyboardMarkup(row_width=5)
n1 = types.InlineKeyboardButton('1', callback_data='1')
n2 = types.InlineKeyboardButton('2', callback_data='2')
n3 = types.InlineKeyboardButton('3', callback_data='3')
n4 = types.InlineKeyboardButton('4', callback_data='4')
n5 = types.InlineKeyboardButton('5', callback_data='5')
n6 = types.InlineKeyboardButton('6', callback_data='6')
n7 = types.InlineKeyboardButton('7', callback_data='7')
n8 = types.InlineKeyboardButton('8', callback_data='8')
n9 = types.InlineKeyboardButton('9', callback_data='9')
n10 = types.InlineKeyboardButton('10', callback_data='10')
n11 = types.InlineKeyboardButton('11', callback_data='11')
n12 = types.InlineKeyboardButton('12', callback_data='12')
n13 = types.InlineKeyboardButton('13', callback_data='13')
n14 = types.InlineKeyboardButton('14', callback_data='14')
n15 = types.InlineKeyboardButton('15', callback_data='15')
n16 = types.InlineKeyboardButton('16', callback_data='16')
n17 = types.InlineKeyboardButton('17', callback_data='17')
n18 = types.InlineKeyboardButton('18', callback_data='18')
n19 = types.InlineKeyboardButton('19', callback_data='19')
n20 = types.InlineKeyboardButton('20', callback_data='20')
quit_ = types.InlineKeyboardButton('QUIT', callback_data='quit_')
pagin.add(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n10,n12,n13,n14,n15,n16,n17,n18,n19,n20, quit_)



@bot.message_handler(commands =['start'])
def start(message):
    chat_id = message.chat.id
    name = message.from_user.first_name
    bot.send_message(chat_id,f'Приветствую тебя, {name.title()}, на новостном портале Kaktus.media\nНажми на кнопку:', reply_markup=keyboard)

@bot.callback_query_handler(lambda call: True)
def call_data(call):
    chat_id = call.message.chat.id

    if call.data == 'quit_':
        bot.edit_message_text(text="Досвидули", message_id=call.message.message_id, chat_id=chat_id)
    if call.data == 'ALL_NEWS':
        bot.edit_message_text(text=f'Выберите новость: ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=pagin)
    if call.data == 'BACK':
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=pagin)
    if call.data == 'photo1':
        bot.edit_message_text(text=f'Новость: {main()[2][0]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back1)
    if call.data == 'link1':
        bot.edit_message_text(text=f'Новость: {main()[0][0]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back1)

    if call.data == 'link2':
        bot.edit_message_text(text=f'Новость: {main()[0][1]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back2)
    if call.data == 'photo3':
        bot.edit_message_text(text=f'Новость: {main()[2][1]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back3)
    if call.data == 'link3':
        bot.edit_message_text(text=f'Новость: {main()[0][2]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back3)

    if call.data == 'link4':
        bot.edit_message_text(text=f'Новость: {main()[0][3]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back4)
    if call.data == 'photo5':
        bot.edit_message_text(text=f'Новость: {main()[2][3]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back5)
    if call.data == 'link5':
        bot.edit_message_text(text=f'Новость: {main()[0][4]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back5)

    if call.data == 'link6':
        bot.edit_message_text(text=f'Новость: {main()[0][5]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back6)
    if call.data == 'photo7':
        bot.edit_message_text(text=f'Новость: {main()[2][4]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back7)
    if call.data == 'link7':
        bot.edit_message_text(text=f'Новость: {main()[0][6]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back7)

    if call.data == 'link8':
        bot.edit_message_text(text=f'Новость: {main()[0][7]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back8)
    if call.data == 'photo9':
        bot.edit_message_text(text=f'Новость: {main()[2][5]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back9)
    if call.data == 'link9':
        bot.edit_message_text(text=f'Новость: {main()[0][8]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back9)

    if call.data == 'link10':
        bot.edit_message_text(text=f'Новость: {main()[0][9]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back10)
    if call.data == 'photo11':
        bot.edit_message_text(text=f'Новость: {main()[2][6]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back11)
    if call.data == 'link11':
        bot.edit_message_text(text=f'Новость: {main()[0][10]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back11)

    if call.data == 'link12':
        bot.edit_message_text(text=f'Новость: {main()[0][11]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back12)
    if call.data == 'photo13':
        bot.edit_message_text(text=f'Новость: {main()[2][7]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back13)
    if call.data == 'link13':
        bot.edit_message_text(text=f'Новость: {main()[0][12]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back13)

    if call.data == 'link14':
        bot.edit_message_text(text=f'Новость: {main()[0][13]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back14)
    if call.data == 'photo15':
        bot.edit_message_text(text=f'Новость: {main()[2][8]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back15)
    if call.data == 'link15':
        bot.edit_message_text(text=f'Новость: {main()[0][14]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back15)

    if call.data == 'link16':
        bot.edit_message_text(text=f'Новость: {main()[0][15]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back16)
    if call.data == 'photo17':
        bot.edit_message_text(text=f'Новость: {main()[2][9]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back17)
    if call.data == 'link17':
        bot.edit_message_text(text=f'Новость: {main()[0][16]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back17)

    if call.data == 'link18':
        bot.edit_message_text(text=f'Новость: {main()[0][17]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back18)
    if call.data == 'photo19':
        bot.edit_message_text(text=f'Новость: {main()[2][10]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back19)
    if call.data == 'link19':
        bot.edit_message_text(text=f'Новость: {main()[0][18]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back19)

    if call.data == 'link20':
        bot.edit_message_text(text=f'Новость: {main()[0][19]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back20)
    if call.data == '1':
        bot.edit_message_text(text=f'Новость: {main()[1][0]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back1)
    if call.data == '2':
        bot.edit_message_text(text=f'Новость: {main()[1][1]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back2)
    if call.data == '3':
        bot.edit_message_text(text=f'Новость: {main()[1][2]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back3)
    if call.data == '4':
        bot.edit_message_text(text=f'Новость: {main()[1][3]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back4)
    if call.data == '5':
        bot.edit_message_text(text=f'Новость: {main()[1][4]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back5)
    if call.data == '6':
        bot.edit_message_text(text=f'Новость: {main()[1][5]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back6)
    if call.data == '7':
        bot.edit_message_text(text=f'Новость: {main()[1][6]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back7)
    if call.data == '8':
        bot.edit_message_text(text=f'Новость: {main()[1][7]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back8)
    if call.data == '9':
        bot.edit_message_text(text=f'Новость: {main()[1][8]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back9)
    if call.data == '10':
        bot.edit_message_text(text=f'Новость: {main()[1][9]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back10)
    if call.data == '11':
        bot.edit_message_text(text=f'Новость: {main()[1][10]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back11)
    if call.data == '12':
        bot.edit_message_text(text=f'Новость: {main()[1][11]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back12)
    if call.data == '13':
        bot.edit_message_text(text=f'Новость: {main()[1][12]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back13)
    if call.data == '14':
        bot.edit_message_text(text=f'Новость: {main()[1][13]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back14)
    if call.data == '15':
        bot.edit_message_text(text=f'Новость: {main()[1][14]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back15)
    if call.data == '16':
        bot.edit_message_text(text=f'Новость: {main()[1][15]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back16)
    if call.data == '17':
        bot.edit_message_text(text=f'Новость: {main()[1][16]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back17)
    if call.data == '18':
        bot.edit_message_text(text=f'Новость: {main()[1][17]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back18)
    if call.data == '19':
        bot.edit_message_text(text=f'Новость: {main()[1][18]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back19)
    if call.data == '20':
        bot.edit_message_text(text=f'Новость: {main()[1][19]} ', message_id=call.message.message_id, chat_id=chat_id)
        bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=chat_id, reply_markup=back20)
bot.polling()
