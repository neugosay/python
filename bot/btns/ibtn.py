from aiogram import types

nazadr = types.KeyboardButton('🔴 Назад')
nazadu = types.KeyboardButton('🔴 Orqaga')
nazade = types.KeyboardButton('🔴 Back')
nazadar = types.KeyboardButton('🔴 العودة')

keyboardr = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboardr.add(types.KeyboardButton("🗑В корзину"), nazadr)

keyboardr2 = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboardr2.add(types.KeyboardButton("Отправить"), types.KeyboardButton("Удалить")).add(nazadr)
#
keyboardu = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboardu.add(types.KeyboardButton("🗑Savatga"), nazadu)

keyboardu2 = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboardu2.add(types.KeyboardButton("Yuborish"), types.KeyboardButton("Olib tashlash")).add(nazadu)
#
keyboarde = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboarde.add(types.KeyboardButton("🗑Into a basket"), nazade)

keyboarde2 = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboarde2.add(types.KeyboardButton("To send"), types.KeyboardButton("Remove")).add(nazade)
#
keyboardar = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboardar.add(types.KeyboardButton("🗑 في سلة"), nazadar)

keyboardar2 = types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard = True)
keyboardar2.add(types.KeyboardButton("إرسال"), types.KeyboardButton("إزالة")).add(nazadar)