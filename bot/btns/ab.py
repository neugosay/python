from aiogram import types

def funr(user_id):
    quest = types.InlineKeyboardMarkup(row_width=2)
    quest.add(
        types.InlineKeyboardButton(text='✅', callback_data=f'{user_id}-ansr'),
        types.InlineKeyboardButton(text='❎', callback_data=f'{user_id}-otkazr'),
    )
    return quest

def funu(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='✅', callback_data=f'{user_id}-ansu'),
        types.InlineKeyboardButton(text='❎', callback_data=f'{user_id}-otkazu')
    )
    return quest

def fune(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='✅', callback_data=f'{user_id}-anse'),
        types.InlineKeyboardButton(text='❎', callback_data=f'{user_id}-otkaze')
    )
    return quest

def funar(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='✅', callback_data=f'{user_id}-ansar'),
        types.InlineKeyboardButton(text='❎', callback_data=f'{user_id}-otkazar')
    )
    return quest

lang = types.ReplyKeyboardMarkup(resize_keyboard=True)
lang.add(
    types.KeyboardButton('🇷🇺 Русский'),
    types.KeyboardButton("🇺🇿 O'zbekcha"),
    types.KeyboardButton('🇺🇸 English'),
    types.KeyboardButton('🇦🇪 العربية')
)

gorod = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
gorod.add(
    types.KeyboardButton('Dubai'),
)