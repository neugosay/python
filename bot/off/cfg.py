from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5896520952:AAF71MR8pMZgZtakbNdR0SJLjOGoybJP8jk'

kolvos = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '🔴 Назад', '🔴 Orqaga']

admin = 5790847484

lang = {
	0:'oof',
	1:'Русский',
	2:"O'zbek",
	3:'English',
	4:'العربية'}

storage = MemoryStorage()
class getkolvo(StatesGroup):
    kolvo = State()
    item = State()
    item2 = State()
    rossilka = State()
    adds = State()
    dadds = State()

photo1 = 'AgACAgIAAxkBAAIIH2OoBFGBBvYrJcwNssOyQdHcuGCNAAIQxzEbJu1BSSfRaXJKiGxHAQADAgADeQADLAQ'
photo2 = 'AgACAgQAAxkBAAIJwGOpumNPclue7SVrO5ztZoB-FjjnAAJXuzEbflf4UAeOCPZceKanAQADAgADeQADLAQ'
photo3 = 'AgACAgQAAxkBAAIJ-WOpyGNhqSXyr7pkvm4PXLT_PeTFAAJSuzEbflf4UFoDCAEW87IYAQADAgADeQADLAQ'
#
photo4 = 'AgACAgQAAxkBAAIKGmOpyOTIkJi5LGnFdSA6ctto2FksAAJZuzEbflf4ULPBzQLBks8NAQADAgADeQADLAQ'
photo5 = 'AgACAgQAAxkBAAIKI2OpydmjhsWxwycz9X_4KX-3gZPDAAJhuzEbflf4UAyJ1KyhCV1cAQADAgADeQADLAQ'
photo6 = 'AgACAgQAAxkBAAIKJWOpyfi5t_609kcc46cybODkZCtLAAJfuzEbflf4UFgdc42jpLs9AQADAgADeQADLAQ'
#
photo7 = 'AgACAgQAAxkBAAILCGOp0t-edZ3KEVSI9Ph7zlET-YKLAAJYuzEbflf4UO0Rd9G_1lspAQADAgADeQADLAQ'
photo8 = 'AgACAgQAAxkBAAILBWOp0t-4BKvIf1KqGd_VGz1WtThJAAJbuzEbflf4UMyk2_eYTXbYAQADAgADeQADLAQ'
photo9 = 'AgACAgQAAxkBAAILGGOp0t9jxu2nG7ouVHWCOOe1bf1JAAJeuzEbflf4UMjPnhsE9rRmAQADAgADeQADLAQ'
photo10 = 'AgACAgQAAxkBAAILBmOp0t_iyECfxBUc3H8QbN6YJcXiAAJcuzEbflf4UHMkwVSZ6RHkAQADAgADeQADLAQ'
photo11 = 'AgACAgQAAxkBAAILC2Op0t8PTWv_omwfnivOAnsU0l-1AAJQuzEbflf4UOtX8pfIn88dAQADAgADeQADLAQ'
photo12 = 'AgACAgQAAxkBAAILDGOp0t8wkhVh-47DV-B53YHLKdthAAJPuzEbflf4UK0xJhilKco_AQADAgADeQADLAQ'
photo13 = 'AgACAgQAAxkBAAILCmOp0t8QPFOyrOat8U5erpp4WMq8AAJRuzEbflf4UPQVgkRzp_13AQADAgADeQADLAQ'
photo14 = 'AgACAgQAAxkBAAILGmOp0t-Cqypdz0NFDzRGA6VZN_2BAAJduzEbflf4UAVmaKT9FR1vAQADAgADeQADLAQ'
photo15 = 'AgACAgQAAxkBAAILD2Op0t8KBJ2mEqdBeD6ep7MIAAEMFwACVbsxG35X-FBbuwGMaUQDXgEAAwIAA3kAAywE'
photo16 = 'AgACAgQAAxkBAAILGWOp0t90NqoJd7b3a7FlmJY_vygwAAJluzEbflf4UBFFSKe6YoB9AQADAgADeQADLAQ'
photo17 = 'AgACAgQAAxkBAAILDmOp0t9qHrAc4LmVPkQZNMNRM9_8AAJjuzEbflf4UA6k-NLHDxseAQADAgADeQADLAQ'
photo18 = 'AgACAgQAAxkBAAILDWOp0t9sE83nyKtYxY1-UJUyMWoYAAJiuzEbflf4UO1NNOUo_F26AQADAgADeQADLAQ'
#
photo19 = 'AgACAgQAAxkBAAILE2Op0t-gMcehOICvry6dmPd2YWWbAAJWuzEbflf4UIWfTN7JAQJSAQADAgADeQADLAQ'
photo20 = 'AgACAgQAAxkBAAILFGOp0t_qvXl4pN11l44ZTU0hQ_hJAAJTuzEbflf4UCu1hkpNmzEvAQADAgADeQADLAQ'
photo21 = 'AgACAgQAAxkBAAILFWOp0t_jFxW-js0DZmy0RL5Ujhc4AAJUuzEbflf4UD3tWXiX4cTHAQADAgADeQADLAQ'
#
photo22 = 'AgACAgQAAxkBAAILCWOp0t-rBQZcMJD1rJUs56g7FWWUAAJOuzEbflf4UAgiibG8FrrbAQADAgADeQADLAQ'

zakaz1por = 'Цена: 0\nОписание: SET'
zakaz2por = 'Цена: 0\nОписание: SET'
zakaz3por = 'Цена: 0\nОписание: SET'
zakaz4por = 'Цена: 0\nОписание: SET'
zakaz5por = 'Цена: 0\nОписание: SET'
zakaz6por = 'Цена: 0\nОписание: SET'
zakaz7por = 'Цена: 0\nОписание: SET'
zakaz8por = 'Цена: 0\nОписание: SET'
zakaz9por = 'Цена: 0\nОписание: SET'
zakaz10por = 'Цена: 0\nОписание: SET'
zakaz11por = 'Цена: 0\nОписание: SET'
zakaz12por = 'Цена: 0\nОписание: SET'
zakaz13por = 'Цена: 0\nОписание: SET'
zakaz14por = 'Цена: 0\nОписание: SET'
zakaz15por = 'Цена: 0\nОписание: SET'
zakaz16por = 'Цена: 0\nОписание: SET'
zakaz17por = 'Цена: 0\nОписание: SET'
zakaz18por = 'Цена: 0\nОписание: SET'
zakaz19por = 'Цена: 0\nОписание: SET'
zakaz20por = 'Цена: 0\nОписание: SET'
zakaz21por = 'Цена: 0\nОписание: SET'
zakaz22por = 'Цена: 0\nОписание: SET'
zakaz23por = 'Цена: 0\nОписание: SET'

zakaz1pou = "Narx: 0\nTa'rif: SET"
zakaz2pou = "Narx: 0\nTa'rif: SET"
zakaz3pou = "Narx: 0\nTa'rif: SET"
zakaz4pou = "Narx: 0\nTa'rif: SET"
zakaz5pou = "Narx: 0\nTa'rif: SET"
zakaz6pou = "Narx: 0\nTa'rif: SET"
zakaz7pou = "Narx: 0\nTa'rif: SET"
zakaz8pou = "Narx: 0\nTa'rif: SET"
zakaz9pou = "Narx: 0\nTa'rif: SET"
zakaz10pou = "Narx: 0\nTa'rif: SET"
zakaz11pou = "Narx: 0\nTa'rif: SET"
zakaz12pou = "Narx: 0\nTa'rif: SET"
zakaz13pou = "Narx: 0\nTa'rif: SET"
zakaz14pou = "Narx: 0\nTa'rif: SET"
zakaz15pou = "Narx: 0\nTa'rif: SET"
zakaz16pou = "Narx: 0\nTa'rif: SET"
zakaz17pou = "Narx: 0\nTa'rif: SET"
zakaz18pou = "Narx: 0\nTa'rif: SET"
zakaz19pou = "Narx: 0\nTa'rif: SET"
zakaz20pou = "Narx: 0\nTa'rif: SET"
zakaz21pou = "Narx: 0\nTa'rif: SET"
zakaz22pou = "Narx: 0\nTa'rif: SET"
zakaz23pou = "Narx: 0\nTa'rif: SET"

zakaz1poe = 'Price: 0\nDescription: SET'
zakaz2poe = 'Price: 0\nDescription: SET'
zakaz3poe = 'Price: 0\nDescription: SET'
zakaz4poe = 'Price: 0\nDescription: SET'
zakaz5poe = 'Price: 0\nDescription: SET'
zakaz6poe = 'Price: 0\nDescription: SET'
zakaz7poe = 'Price: 0\nDescription: SET'
zakaz8poe = 'Price: 0\nDescription: SET'
zakaz9poe = 'Price: 0\nDescription: SET'
zakaz10poe = 'Price: 0\nDescription: SET'
zakaz11poe = 'Price: 0\nDescription: SET'
zakaz12poe = 'Price: 0\nDescription: SET'
zakaz13poe = 'Price: 0\nDescription: SET'
zakaz14poe = 'Price: 0\nDescription: SET'
zakaz15poe = 'Price: 0\nDescription: SET'
zakaz16poe = 'Price: 0\nDescription: SET'
zakaz17poe = 'Price: 0\nDescription: SET'
zakaz18poe = 'Price: 0\nDescription: SET'
zakaz19poe = 'Price: 0\nDescription: SET'
zakaz20poe = 'Price: 0\nDescription: SET'
zakaz21poe = 'Price: 0\nDescription: SET'
zakaz22poe = 'Price: 0\nDescription: SET'
zakaz23poe = 'Price: 0\nDescription: SET'

zakaz1poar = 'السعر: 0\nالوصف: SET'
zakaz2poar = 'السعر: 0\nالوصف: SET'
zakaz3poar = 'السعر: 0\nالوصف: SET'
zakaz4poar = 'السعر: 0\nالوصف: SET'
zakaz5poar = 'السعر: 0\nالوصف: SET'
zakaz6poar = 'السعر: 0\nالوصف: SET'
zakaz7poar = 'السعر: 0\nالوصف: SET'
zakaz8poar = 'السعر: 0\nالوصف: SET'
zakaz9poar = 'السعر: 0\nالوصف: SET'
zakaz10poar = 'السعر: 0\nالوصف: SET'
zakaz11poar = 'السعر: 0\nالوصف: SET'
zakaz12poar = 'السعر: 0\nالوصف: SET'
zakaz13poar = 'السعر: 0\nالوصف: SET'
zakaz14poar = 'السعر: 0\nالوصف: SET'
zakaz15poar = 'السعر: 0\nالوصف: SET'
zakaz16poar = 'السعر: 0\nالوصف: SET'
zakaz17poar = 'السعر: 0\nالوصف: SET'
zakaz18poar = 'السعر: 0\nالوصف: SET'
zakaz19poar = 'السعر: 0\nالوصف: SET'
zakaz20poar = 'السعر: 0\nالوصف: SET'
zakaz21poar = 'السعر: 0\nالوصف: SET'
zakaz22poar = 'السعر: 0\nالوصف: SET'
zakaz23poar = 'السعر: 0\nالوصف: SET'
