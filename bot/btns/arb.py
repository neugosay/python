from aiogram import types

glmen = types.KeyboardButton('🔴 القائمة الرئيسية')
nazad = types.KeyboardButton('🔴 العودة')

nomer = types.KeyboardButton('ارسل الرقم', request_contact = True)
lol = types.ReplyKeyboardMarkup(resize_keyboard = True).add(nomer)
loc = types.KeyboardButton('إرسال الموقع الجغرافي', request_location = True)
lol2 = types.ReplyKeyboardMarkup(resize_keyboard = True).add(loc)

glmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
glmenu.add(types.KeyboardButton('🛍 لأجل')).add(types.KeyboardButton('🗑سلة')).add(types.KeyboardButton('⚙️ الإعدادات'))

settings = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
settings.add(types.KeyboardButton('🇦🇪 تغيير اللغة')).add(glmen)

kategorii = types.ReplyKeyboardMarkup(resize_keyboard=True)
kategorii.add(types.KeyboardButton('الدورات الأولى'), types.KeyboardButton('الدورات الثانية')).add(types.KeyboardButton('أطباق اللحوم'), types.KeyboardButton('السلطات')).add(types.KeyboardButton('المشروبات')).add(nazad)

odinblydo1 = types.KeyboardButton('حساء لحم البقر')
odinblydo2 = types.KeyboardButton('حساء ماستافا')
odinblydo3 = types.KeyboardButton('طبق لاجمان')
odinblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(odinblydo1, odinblydo2).add(odinblydo3).add(nazad)

dwablydo1 = types.KeyboardButton('فرايد لاجمان')
dwablydo2 = types.KeyboardButton('طبق مانتا راي')
dwablydo3 = types.KeyboardButton('طبق دولما')
dwablydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(dwablydo1, dwablydo2).add(dwablydo3).add(nazad)

myasoblydo1 = types.KeyboardButton('خروف في التندور')
myasoblydo2 = types.KeyboardButton('كباب الدجاج')
myasoblydo3 = types.KeyboardButton('تكا بوتي')
myasoblydo4 = types.KeyboardButton('كباب لحم')
myasoblydo5 = types.KeyboardButton('الخبز مع الدجاج')
myasoblydo6 = types.KeyboardButton('خبز باللحم')
myasoblydo7 = types.KeyboardButton('الخبز مع كباب شيش')
myasoblydo8 = types.KeyboardButton('دجاج التندور (نصف)')
myasoblydo9 = types.KeyboardButton('دجاج التندور (كامل)')
myasoblydo10 = types.KeyboardButton('سوبر بيلاف كومبو')
myasoblydo11 = types.KeyboardButton('طبق بيلاف')
myasoblydo12 = types.KeyboardButton('عرض بيلاف')
myasoblydo = types.ReplyKeyboardMarkup(resize_keyboard=True).add(myasoblydo1, myasoblydo2).add(myasoblydo3, myasoblydo4).add(
    myasoblydo5, myasoblydo6).add(myasoblydo7, myasoblydo8).add(myasoblydo9, myasoblydo10).add(myasoblydo11, myasoblydo12).add(nazad)

salat1 = types.KeyboardButton('اليونانية')
salat2 = types.KeyboardButton('صلصة الخل')
salat3 = types.KeyboardButton('أوليفييه')
salats = types.ReplyKeyboardMarkup(resize_keyboard=True).add(salat1, salat2).add(salat3).add(nazad)

napitki1 = types.KeyboardButton('موريلو الكرز')
napitki2 = types.KeyboardButton('عصير الليمون')
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