from aiogram import types

glmen = types.KeyboardButton('🔴 Main menu')
nazad = types.KeyboardButton('🔴 Back')

nomer = types.KeyboardButton('Send Number', request_contact = True)
lol = types.ReplyKeyboardMarkup(resize_keyboard = True).add(nomer)
loc = types.KeyboardButton('Send geolocation', request_location = True)
lol2 = types.ReplyKeyboardMarkup(resize_keyboard = True).add(loc)

button1 = types.KeyboardButton('🛍 To order')
button2 = types.KeyboardButton('🗑Basket')
button3 = types.KeyboardButton('⚙️ Settings')
glmenu = types.ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button2).add(button3)

lang = types.KeyboardButton('🇺🇸 Change the language')
settings = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(lang).add(glmen)

zak1 = types.KeyboardButton('First courses')
zak2 = types.KeyboardButton('Second courses')
zak3 = types.KeyboardButton('Meat dishes')
zak4 = types.KeyboardButton('Salads')
zak5 = types.KeyboardButton('Drinks')
kategorii = types.ReplyKeyboardMarkup(resize_keyboard=True).add(zak1, zak2).add(zak3, zak4).add(zak5).add(glmen)

dwablydo1 = types.KeyboardButton("Fried Lagman")
dwablydo2 = types.KeyboardButton("Manta ray dish")
dwablydo3 = types.KeyboardButton('Dolma dish')
dwablydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(dwablydo1, dwablydo2).add(dwablydo3).add(glmen)

odinblydo1 = types.KeyboardButton('Beef soup')
odinblydo2 = types.KeyboardButton('Mastava soup')
odinblydo3 = types.KeyboardButton('Lagman dish')
odinblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(odinblydo1, odinblydo2).add(odinblydo3).add(glmen)

myasoblydo1 = types.KeyboardButton('Lamb in a tandoor')
myasoblydo2 = types.KeyboardButton('Chicken kebab')
myasoblydo3 = types.KeyboardButton('Meat kebab')
myasoblydo4 = types.KeyboardButton('Honey kebab')
myasoblydo5 = types.KeyboardButton('Chicken kebab')
myasoblydo5 = types.KeyboardButton('Bread with chicken')
myasoblydo6 = types.KeyboardButton('Bread with meat')
myasoblydo7 = types.KeyboardButton('Bread with cupcake')
myasoblydo8 = types.KeyboardButton('Tandoor chicken (HALF)')
myasoblydo9 = types.KeyboardButton('Tandoor chicken (WHOLE)')
myasoblydo10 = types.KeyboardButton('Super pilaf combo')
myasoblydo11 = types.KeyboardButton('Pilaf dish')
myasoblydo12 = types.KeyboardButton('Pilaf offer')
myasoblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(myasoblydo1, myasoblydo2).add(myasoblydo3, myasoblydo4).add(
    myasoblydo5, myasoblydo6).add(myasoblydo7, myasoblydo8).add(myasoblydo9, myasoblydo10).add(myasoblydo11, myasoblydo12).add(glmen)

salat1 = types.KeyboardButton('Greek')
salat2 = types.KeyboardButton('Vinigret')
salat3 = types.KeyboardButton('Olivier')
salats = types.ReplyKeyboardMarkup(resize_keyboard=True).add(salat1, salat2).add(salat3).add(glmen)

napitki1 = types.KeyboardButton('Morello Cherry')
napitki2 = types.KeyboardButton('Limonade')
napitki = types.ReplyKeyboardMarkup(resize_keyboard=True).add(napitki1, napitki2).add(glmen)

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