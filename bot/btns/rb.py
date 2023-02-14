from aiogram import types

glmen = types.KeyboardButton('🔴 Главное меню')
nazad = types.KeyboardButton('🔴 Назад')

nomer = types.KeyboardButton('Отправить номер', request_contact = True)
lol = types.ReplyKeyboardMarkup(resize_keyboard = True).add(nomer)
loc = types.KeyboardButton('Отправить геолокацию', request_location = True)
lol2 = types.ReplyKeyboardMarkup(resize_keyboard = True).add(loc)

glmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
glmenu.add(types.KeyboardButton('🛍 Заказать')).add(types.KeyboardButton('🗑Корзина')).add(types.KeyboardButton('⚙️ Настройки'))

settings = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
settings.add(types.KeyboardButton('🇷🇺 Изменить язык')).add(glmen)

kategorii = types.ReplyKeyboardMarkup(resize_keyboard=True)
kategorii.add(types.KeyboardButton('Первые блюда'), types.KeyboardButton('Вторые блюда')).add(types.KeyboardButton('Мясные блюда'), types.KeyboardButton('Салаты')).add(types.KeyboardButton('Напитки')).add(nazad)

odinblydo1 = types.KeyboardButton('Суп из говядины')
odinblydo2 = types.KeyboardButton('Суп из маставы')
odinblydo3 = types.KeyboardButton('Блюдо из лагмана')
odinblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(odinblydo1, odinblydo2).add(odinblydo3).add(nazad)

dwablydo1 = types.KeyboardButton('Лагман жареный')
dwablydo2 = types.KeyboardButton('Блюдо из мантов')
dwablydo3 = types.KeyboardButton('Блюдо из долмы')
dwablydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(dwablydo1, dwablydo2).add(dwablydo3).add(nazad)

myasoblydo1 = types.KeyboardButton('Ягнёнок в тандыре')
myasoblydo2 = types.KeyboardButton('Куриный шашлык')
myasoblydo3 = types.KeyboardButton('Тикка Боти')
myasoblydo4 = types.KeyboardButton('Мясной шашлык')
myasoblydo5 = types.KeyboardButton('Хлеб с цыпленком')
myasoblydo6 = types.KeyboardButton('Хлеб с мясом')
myasoblydo7 = types.KeyboardButton('Хлеб с кекабом')
myasoblydo8 = types.KeyboardButton('Тандырная курица (ПОЛОВИНА)')
myasoblydo9 = types.KeyboardButton('Тандырная курица (ЦЕЛАЯ)')
myasoblydo10 = types.KeyboardButton('Супер плов комбо')
myasoblydo11 = types.KeyboardButton('Блюдо из плова')
myasoblydo12 = types.KeyboardButton('Предложение плова')
myasoblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(myasoblydo1, myasoblydo2).add(myasoblydo3, myasoblydo4).add(
    myasoblydo5, myasoblydo6).add(myasoblydo7, myasoblydo8).add(myasoblydo9, myasoblydo10).add(myasoblydo11, myasoblydo12).add(nazad)

salat1 = types.KeyboardButton('Греческий')
salat2 = types.KeyboardButton('Винигрет')
salat3 = types.KeyboardButton('Оливье')
salats = types.ReplyKeyboardMarkup(resize_keyboard=True).add(salat1, salat2).add(salat3).add(nazad)

napitki1 = types.KeyboardButton('Morello Cherry')
napitki2 = types.KeyboardButton('Limonade')
napitki = types.ReplyKeyboardMarkup(resize_keyboard=True).add(napitki1, napitki2).add(nazad)


was1 = types.KeyboardButton('1')
was2 = types.KeyboardButton('2')
was3 = types.KeyboardButton('3')
was4 = types.KeyboardButton('4')
was5 = types.KeyboardButton('5')
was6 = types.KeyboardButton('6')
was7 = types.KeyboardButton('7')
was8 = types.KeyboardButton('8')
was9 = types.KeyboardButton('9')
was10 = types.KeyboardButton('10')
setkolvo = types.ReplyKeyboardMarkup(resize_keyboard = True).add(was1).add(was2).add(was3).add(was4).add(was5).add(was6).add(was7).add(was8).add(was9).add(was10).add(nazad)

adm1 = types.KeyboardButton('Рассылка')
adm = types.ReplyKeyboardMarkup(resize_keyboard=True).add(adm1)