from aiogram import types

nazad = types.KeyboardButton('🔴 Orqaga')
glmen = types.KeyboardButton('🔴 Asosiy menyu')

nomer = types.KeyboardButton('Raqamni yuboring', request_contact = True)
lol = types.ReplyKeyboardMarkup(resize_keyboard = True).add(nomer)
loc = types.KeyboardButton('Geolokatsiyani yuborish', request_location = True)
lol2 = types.ReplyKeyboardMarkup(resize_keyboard = True).add(loc)

glmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
glmenu.add(types.KeyboardButton('🛍 Buyurtma berish')).add(types.KeyboardButton('🗑Savat')).add(types.KeyboardButton('⚙️ Sozlamalar'))

settings = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
settings.add(types.KeyboardButton("🇺🇿 Tilni o'zgartirish")).add(glmen)

kategorii = types.ReplyKeyboardMarkup(resize_keyboard=True)
kategorii.add(types.KeyboardButton('Birinchi kurslar'), types.KeyboardButton('Ikkinchi kurslar')).add(types.KeyboardButton("Go'shtli idishlar"), types.KeyboardButton('Salatlar')).add(types.KeyboardButton('Ichimliklar')).add(glmen)

odinblydo1 = types.KeyboardButton("Mol go'shti sho'rvasi")
odinblydo2 = types.KeyboardButton("Mastava sho'rva")
odinblydo3 = types.KeyboardButton('Lagman taomlari')
odinblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(odinblydo1, odinblydo2).add(odinblydo3).add(glmen)

dwablydo1 = types.KeyboardButton("Lagman qovurilgan")
dwablydo2 = types.KeyboardButton("Manti taomlari")
dwablydo3 = types.KeyboardButton('Dolma taom')
dwablydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(dwablydo1, dwablydo2).add(dwablydo3).add(glmen)

myasoblydo1 = types.KeyboardButton("Tandirda qo'zichoq")
myasoblydo2 = types.KeyboardButton('Tovuq kaboblari')
myasoblydo3 = types.KeyboardButton('Tikka Boti')
myasoblydo4 = types.KeyboardButton("Go'shtli shish")
myasoblydo5 = types.KeyboardButton('Tovuq bilan non')
myasoblydo6 = types.KeyboardButton("Go'sht bilan non")
myasoblydo7 = types.KeyboardButton('Kekab bilan non')
myasoblydo8 = types.KeyboardButton('Tandir Tovuqi (yarim)')
myasoblydo9 = types.KeyboardButton('Tandir Tovuqi (butun)')
myasoblydo10 = types.KeyboardButton('Super palov kombinati')
myasoblydo11 = types.KeyboardButton('Palovdan tayyorlangan taom')
myasoblydo12 = types.KeyboardButton('Palov taklifi')
myasoblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(myasoblydo1, myasoblydo2).add(myasoblydo3, myasoblydo4).add(
    myasoblydo5, myasoblydo6).add(myasoblydo7, myasoblydo8).add(myasoblydo9, myasoblydo10).add(myasoblydo11, myasoblydo12).add(glmen)

salat1 = types.KeyboardButton('Yunon')
salat2 = types.KeyboardButton('Vinaigrette')
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

adm1 = types.KeyboardButton('Рассылка')
adm = types.ReplyKeyboardMarkup(resize_keyboard=True).add(adm1)