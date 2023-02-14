from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher, FSMContext
import logging
from off import cfg, db
from btns import ab, eb, rb, ub, ibtn, arb

logging.basicConfig(level=logging.INFO)
bot = Bot(token = cfg.TOKEN)
dp = Dispatcher(bot, storage=cfg.storage)
db.creater()

@dp.message_handler(commands = ['addid'])
async def add(message: types.Message):
	if message.from_user.id == cfg.admin:
		await bot.send_message(message.from_user.id, 'Please enter the user id')
		await cfg.getkolvo.adds.set()

@dp.message_handler(commands = ['dellid'])
async def add(message: types.Message):
	if message.from_user.id == cfg.admin:
		await bot.send_message(message.from_user.id, 'Please enter the user id')
		await cfg.getkolvo.dadds.set()

@dp.message_handler(commands = ['start'])
async def cmd_start(message: types.Message):
	if not db.user_exists(message.from_user.id):
		db.kur.execute(f"INSERT INTO Accounts VALUES ({message.from_user.id},'{message.from_user.first_name}', 0, 0, 0, 0, 0, 0, 0, 0)")
		db.db.commit()        
		await bot.send_message(message.from_user.id, f'''
Assalomu alaykum! Meat and bread yetkazib berish xizmatiga xush kelibsiz.

Здравствуйте! Добро пожаловать в службу доставки Meat and bread

Hello! Welcome to Meat and bread delivery service.

مرحبا! مرحبا بكم في خدمة توصيل اللحوم والخبز.''', parse_mode='HTML', reply_markup=ab.lang)
	else:
		if db.get_lang(message.from_user.id)[0][0] == 1: await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=rb.glmenu)
		if db.get_lang(message.from_user.id)[0][0] == 2: await bot.send_message(message.from_user.id, 'Asosiy menyu', reply_markup=ub.glmenu)
		if db.get_lang(message.from_user.id)[0][0] == 3: await bot.send_message(message.from_user.id, 'Main Menu', reply_markup=eb.glmenu)
		if db.get_lang(message.from_user.id)[0][0] == 4: await bot.send_message(message.from_user.id, 'القائمة الرئيسية', reply_markup=arb.glmenu)

@dp.message_handler(content_types= ['text'])
async def cmds(message: types.Message):
	if message.text == 'Dubai':
		await shit4(message)
		db.kur.execute(f"UPDATE Accounts SET Gorod = 1 WHERE id={message.from_user.id}")
		db.db.commit()

	#РУССКОЕ МЕНЮ
	if message.text == '🇷🇺 Русский':
		if db.user_langs(message.from_user.id)[0][0] == 1:
			await bot.send_message(message.from_user.id, 'Вы успешно сменили язык', reply_markup=rb.glmenu)
			db.kur.execute(f"UPDATE Accounts SET Lang = 1 WHERE id={message.from_user.id}")
			db.kur.execute(f"UPDATE Accounts SET LangState = 0 WHERE id={message.from_user.id}")
		else: 
			await bot.send_message(message.from_user.id, 'В каком городе вы живёте?\nПожалуйста, выбирите', reply_markup=ab.gorod)
			db.kur.execute(f"UPDATE Accounts SET Lang = 1 WHERE id={message.from_user.id}")
		db.db.commit()

	if message.text == '🛍 Заказать':
		fal(message)
		await bot.send_message(message.from_user.id, 'С чего начнём?', reply_markup=rb.kategorii)

	if message.text == '🗑Корзина':
		if not db.zakaz_get(message.from_user.id):
			await bot.send_message(message.from_user.id, 'У вас нет заказов', reply_markup=rb.glmenu)
		else:
			await shit5(message)

	if message.text == '⚙️ Настройки': await bot.send_message(message.from_user.id, 'Выберите действие:', reply_markup=rb.settings)

	if message.text == '🇷🇺 Изменить язык':
		shit2(message)
		await bot.send_message(message.from_user.id, "Выберите язык:", reply_markup=ab.lang)

	if message.text == '🏙 Изменить город': await bot.send_message(message.from_user.id, 'В каком городе вы живёте?\nПожалуйста, выбирите', reply_markup=ab.gorod)

	if message.text == '🔴 Главное меню':
		await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=rb.glmenu)
		shit1(message)

	if message.text == '🔴 Назад':
		shit6(message)
		if db.get_snazad(message.from_user.id)[0][0] == 0: await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = rb.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 1:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 0 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'Главное меню', reply_markup = rb.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 2:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'С чего начнём?', reply_markup = rb.kategorii)
	
	if message.text == 'Первые блюда':
		fal(message)
		await bot.send_message(message.from_user.id, 'Выбирите блюдо:', reply_markup = rb.odinblydo)
	if message.text == 'Вторые блюда':
		fal(message)
		await bot.send_message(message.from_user.id, 'Выбирите блюдо:', reply_markup = rb.dwablydo)
	if message.text == 'Мясные блюда':
		fal(message)
		await bot.send_message(message.from_user.id, 'Выбирите блюдо:', reply_markup = rb.myasoblydo)
	if message.text == 'Салаты':
		fal(message)
		await bot.send_message(message.from_user.id, 'Выбирите блюдо:', reply_markup = rb.salats)
	if message.text == 'Напитки':
		fal(message)
		await bot.send_message(message.from_user.id, 'Выбирите блюдо:', reply_markup = rb.napitki)

	if message.text == "Удалить":
		await bot.send_message(message.from_user.id, 'Вы успешно удалили.', reply_markup = rb.glmenu)
		db.kur.execute(f'DELETE FROM Zakaz WHERE ID = {message.from_user.id}')
		db.db.commit()

	if message.text == 'Отправить':
		await bot.send_message(message.from_user.id, 'Ожидайте ответа.', reply_markup=rb.glmenu)
		db.kur.execute(f"SELECT ID FROM VSE")
		row = db.kur.fetchall()
		db.db.commit()
		info = row
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], f'''Поступил новый заказ!

Имя • <b>{db.get_name(message.from_user.id)[0][0]}</b>
Язык • <b>{cfg.lang[db.get_lang(message.from_user.id)[0][0]]}</b>
Номер • <code>+{db.get_num(message.from_user.id)[0][0]}</code>
Локация • <code>{db.get_loc1(message.from_user.id)[0][0]}, {db.get_loc2(message.from_user.id)[0][0]}</code>

Заказы:

Суп из говядины • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
Суп из маставы • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
Блюдо из лагмана • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

Лагман жареный • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
Блюдо из мантов • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
Блюдо из долмы • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

Ягнёнок в тандыре • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
Куриный шашлык • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
Тикка Боти • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
Мясной шашлык • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
Хлеб с цыпленком • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
Хлеб с мясом • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
Хлеб с кекабом • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
Тандырная курица (ПОЛОВИНА) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
Тандырная курица (ЦЕЛАЯ) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
Супер плов комбо • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
Блюдо из плова • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
Предложение плова • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

Греческий салат • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
Винигрет • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
Оливье • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

Morello Cherry • {db.get_zakaz22(message.from_user.id)[0][0]}
Limonade • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup =ab.funr(message.chat.id))
			except:
				pass

	if message.text == '🗑В корзину':
		if db.get_szakaz(message.from_user.id)[0][0] == 1: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 2: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 3: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 4: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 5: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 6: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 7: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 8: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 9: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 10: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 11: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 12: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 13: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 14: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 15: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 17: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 18: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 19: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 20: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 21: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 22: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 23: await shit3(message)

	if message.text == 'Суп из говядины':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 1 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo1, caption = cfg.zakaz1por, reply_markup = ibtn.keyboardr)

	if message.text == 'Суп из маставы':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 2 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo2, caption = cfg.zakaz2por, reply_markup = ibtn.keyboardr)

	if message.text == 'Блюдо из лагмана':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 3 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo3, caption = cfg.zakaz3por, reply_markup = ibtn.keyboardr)

	if message.text == 'Лагман жареный':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 4 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo4, caption = cfg.zakaz4por, reply_markup = ibtn.keyboardr)

	if message.text == 'Блюдо из мантов':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 5 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo5, caption = cfg.zakaz5por, reply_markup = ibtn.keyboardr)

	if message.text == 'Блюдо из долмы':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 6 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo6, caption = cfg.zakaz6por, reply_markup = ibtn.keyboardr)
	#
	if message.text == 'Ягнёнок в тандыре':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 7 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo7, caption = cfg.zakaz7por, reply_markup = ibtn.keyboardr)
	
	if message.text == 'Куриный шашлык':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 8 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo8, caption = cfg.zakaz8por, reply_markup = ibtn.keyboardr)

	if message.text == 'Тикка Боти':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 9 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo9, caption = cfg.zakaz9por, reply_markup = ibtn.keyboardr)

	if message.text == 'Мясной шашлык':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 10 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo10, caption = cfg.zakaz10por, reply_markup = ibtn.keyboardr)

	if message.text == 'Хлеб с цыпленком':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 11 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo11, caption = cfg.zakaz11por, reply_markup = ibtn.keyboardr)

	if message.text == 'Хлеб с мясом':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 12 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo12, caption = cfg.zakaz12por, reply_markup = ibtn.keyboardr)

	if message.text == 'Хлеб с кекабом':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 13 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo13, caption = cfg.zakaz13por, reply_markup = ibtn.keyboardr)

	if message.text == 'Тандырная курица (ПОЛОВИНА)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 14 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo14, caption = cfg.zakaz14por, reply_markup = ibtn.keyboardr)

	if message.text == 'Тандырная курица (ЦЕЛАЯ)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 15 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo15, caption = cfg.zakaz15por, reply_markup = ibtn.keyboardr)

	if message.text == 'Супер плов комбо':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 16 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo16, caption = cfg.zakaz16por, reply_markup = ibtn.keyboardr)

	if message.text == 'Блюдо из плова':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 17 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo17, caption = cfg.zakaz17por, reply_markup = ibtn.keyboardr)

	if message.text == 'Предложение плова':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 18 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo18, caption = cfg.zakaz18por, reply_markup = ibtn.keyboardr)
	#
	if message.text == 'Греческий':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 19 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo19, caption = cfg.zakaz19por, reply_markup = ibtn.keyboardr)

	if message.text == 'Винигрет':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 20 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo20, caption = cfg.zakaz20por, reply_markup = ibtn.keyboardr)

	if message.text == 'Оливье':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 21 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo21, caption = cfg.zakaz21por, reply_markup = ibtn.keyboardr)

	#
	if message.text == 'Morello Cherry':
		await Morello(message)

	if message.text == 'Выбрать ещё': await bot.send_message(message.from_user.id, 'Выбирите котегорию:', reply_markup = rb.kategorii)

	#УЗБЕКСКОЕ МЕНЮ
	if message.text == "🇺🇿 O'zbekcha":
		if db.user_langs(message.from_user.id)[0][0] == 1:
			await bot.send_message(message.from_user.id, "Siz tilingizni muvaffaqiyatli o'zgartirdingiz", reply_markup=ub.glmenu)
			db.kur.execute(f"UPDATE Accounts SET Lang = 2 WHERE id={message.from_user.id}")
			db.kur.execute(f"UPDATE Accounts SET LangState = 0 WHERE id={message.from_user.id}")
		else: 
			await bot.send_message(message.from_user.id, 'Siz qaysi shaharda yashaysiz?\nIltimos, tanlang', reply_markup=ab.gorod)
			db.kur.execute(f"UPDATE Accounts SET Lang = 2 WHERE id={message.from_user.id}")
		db.db.commit()

	if message.text == '🛍 Buyurtma berish': await bot.send_message(message.from_user.id, 'Qaerdan boshlaymiz?', reply_markup=ub.kategorii)

	if message.text == '🗑Savat':
		if not db.zakaz_get(message.from_user.id):
			await bot.send_message(message.from_user.id, "Sizda buyurtmalar yo'q", reply_markup=ub.glmenu)
		else:
			await shit5(message)

	if message.text == '⚙️ Sozlamalar': await bot.send_message(message.from_user.id, 'Amalni tanlang:', reply_markup=ub.settings)

	if message.text == "🇺🇿 Tilni o'zgartirish":
		shit2(message)
		await bot.send_message(message.from_user.id, "Tilni tanlang:", reply_markup=ab.lang)

	if message.text == "🏙 Shaharni o'zgartirish": await bot.send_message(message.from_user.id, 'Siz qaysi shaharda yashaysiz?\nIltimos, tanlang', reply_markup=ab.gorod)

	if message.text == '🔴 Asosiy menyu':
		await bot.send_message(message.from_user.id, 'Asosiy menyu', reply_markup=ub.glmenu)
		shit1(message)

	if message.text == "Olib tashlash":
		await bot.send_message(message.from_user.id, 'Siz muvaffaqiyatli olib tashladingiz.', reply_markup = ub.glmenu)
		db.kur.execute(f'DELETE FROM Zakaz WHERE ID = {message.from_user.id}')
		db.db.commit()

	if message.text == '🔴 Orqaga':
		shit6(message)
		if db.get_snazad(message.from_user.id)[0][0] == 0: await bot.send_message(message.from_user.id, 'Asosiy menyu', reply_markup = ub.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 1:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 0 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'Asosiy menyu', reply_markup = ub.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 2:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'Qayerdan boshlaymiz?', reply_markup = ub.kategorii)

	if message.text == 'Birinchi kurslar':
		fal(message)
		await bot.send_message(message.from_user.id, 'Taomni tanlang:', reply_markup = ub.odinblydo)
	if message.text == 'Ikkinchi kurslar':
		fal(message)
		await bot.send_message(message.from_user.id, 'Taomni tanlang:', reply_markup = ub.dwablydo)
	if message.text == "Go'shtli idishlar":
		fal(message)
		await bot.send_message(message.from_user.id, 'Taomni tanlang:', reply_markup = ub.myasoblydo)
	if message.text == 'Salatlar':
		fal(message)
		await bot.send_message(message.from_user.id, 'Taomni tanlang:', reply_markup = ub.salats)
	if message.text == 'Ichimliklar':
		fal(message)
		await bot.send_message(message.from_user.id, 'Taomni tanlang:', reply_markup = ub.napitki)

	if message.text == 'Yuborish':
		await bot.send_message(message.from_user.id, 'Javobni kuting.', reply_markup=ub.glmenu)
		db.kur.execute(f"SELECT ID FROM VSE")
		row = db.kur.fetchall()
		db.db.commit()
		info = row
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], f'''Yangi buyurtma keldi!

Ism • <b>{db.get_name(message.from_user.id)[0][0]}</b>
Til • <b>{cfg.lang[db.get_lang(message.from_user.id)[0][0]]}</b>
Raqam • <code>+{db.get_num(message.from_user.id)[0][0]}</code>
Joylashuv • <code>{db.get_loc1(message.from_user.id)[0][0]}, {db.get_loc2(message.from_user.id)[0][0]}</code>

Buyurtmalar:

Mol go'shti sho'rvasi • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
Mastava sho'rva • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
Lagman taomlari • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

Lagman qovurilgan • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
Manti taomlari • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
Dolma taom • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

Tandirda qo'zichoq • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
Tovuq kaboblari • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
Tikka Boti • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
Go'shtli shish • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
Tovuq bilan non • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
Go'sht bilan non • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
Yokab bilan non • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
Tandir Tovuqi (yarim) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
Tandir Tovuqi (butun) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
Super palov kombinati • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
Palovdan tayyorlangan taom • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
Palov taklifi • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

Yunon salatasi • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
Vinaigrette • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
Olivier • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

Morello Cherry • {db.get_zakaz22(message.from_user.id)[0][0]}
Limonade • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup =ab.funu(message.chat.id))
			except:
				pass

	if message.text == '🗑Savatga':
		if db.get_szakaz(message.from_user.id)[0][0] == 1: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 2: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 3: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 4: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 5: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 6: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 7: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 8: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 9: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 10: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 11: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 12: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 13: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 14: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 15: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 17: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 18: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 19: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 20: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 21: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 22: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 23: await shit3(message)
	
	if message.text == "Mol go'shti sho'rvasi":
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 1 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo1, caption = cfg.zakaz1pou, reply_markup = ibtn.keyboardu)

	if message.text == "Mastava sho'rva":
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 2 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo2, caption = cfg.zakaz2pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Lagman taomlari':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 3 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo3, caption = cfg.zakaz3pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Lagman qovurilgan':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 4 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo4, caption = cfg.zakaz4pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Manti taomlari':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 5 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo5, caption = cfg.zakaz5pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Dolma taom':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 6 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo6, caption = cfg.zakaz6pou, reply_markup = ibtn.keyboardu)
	#
	if message.text == "Tandirda qo'zichoq":
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 7 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo7, caption = cfg.zakaz7pou, reply_markup = ibtn.keyboardu)
	
	if message.text == 'Tovuq kaboblari':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 8 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo8, caption = cfg.zakaz8por, reply_markup = ibtn.keyboardu)

	if message.text == 'Tikka Boti':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 9 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo9, caption = cfg.zakaz9pou, reply_markup = ibtn.keyboardu)

	if message.text == "Go'shtli shish":
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 10 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo10, caption = cfg.zakaz10pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Tovuq bilan non':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 11 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo11, caption = cfg.zakaz11pou, reply_markup = ibtn.keyboardu)

	if message.text == "Go'sht bilan non":
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 12 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo12, caption = cfg.zakaz12pou, reply_markup = ibtn.keyboardu)

	if message.text == "Kekab bilan non":
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 13 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo13, caption = cfg.zakaz13pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Tandir Tovuqi (yarim)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 14 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo14, caption = cfg.zakaz14pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Tandir Tovuqi (butun)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 15 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo15, caption = cfg.zakaz15pou, reply_markup = ibtn.keyboardu)

	if message.text == "Super palov kombinati":
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 16 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo16, caption = cfg.zakaz16pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Palovdan tayyorlangan taom':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 17 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo17, caption = cfg.zakaz17pou, reply_markup = ibtn.keyboardu)

	if message.text == 'Palov taklifi':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 18 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo18, caption = cfg.zakaz18pou, reply_markup = ibtn.keyboardu)
	#
	if message.text == 'Yunon':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 19 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo19, caption = cfg.zakaz19pou, reply_markup = ibtn.keyboardu)

	#english
	if message.text == '🇺🇸 English':
		if db.user_langs(message.from_user.id)[0][0] == 1:
			await bot.send_message(message.from_user.id, 'You have successfully changed the language', reply_markup=eb.glmenu)
			db.kur.execute(f"UPDATE Accounts SET Lang = 3 WHERE id={message.from_user.id}")
			db.kur.execute(f"UPDATE Accounts SET LangState = 0 WHERE id={message.from_user.id}")
		else: 
			await bot.send_message(message.from_user.id, 'What city do you live in?\nPlease select', reply_markup=ab.gorod)
			db.kur.execute(f"UPDATE Accounts SET Lang = 3 WHERE id={message.from_user.id}")
		db.db.commit()

	if message.text == '🛍 To order': await bot.send_message(message.from_user.id, 'Where do we start?', reply_markup=eb.kategorii)

	if message.text == '🗑Basket':
		if not db.zakaz_get(message.from_user.id):
			await bot.send_message(message.from_user.id, "You don't have any orders")
		else:
			await shit5(message)

	if message.text == '⚙️ Settings': await bot.send_message(message.from_user.id, 'Select an action:', reply_markup=eb.settings)

	if message.text == '🇺🇸 Change the language':
		shit2(message)
		await bot.send_message(message.from_user.id, "Select a language:", reply_markup=ab.lang)

	if message.text == '🏙 Change the city': await bot.send_message(message.from_user.id, 'What city do you live in?\nPlease select', reply_markup=ab.gorod)

	if message.text == '🔴 Main menu':
		await bot.send_message(message.from_user.id, 'Main menu', reply_markup=eb.glmenu)
		shit1(message)

	if message.text == 'Remove':
		await bot.send_message(message.from_user.id, 'You have successfully deleted.', reply_markup = eb.glmenu)
		db.kur.execute(f'DELETE FROM Zakaz WHERE ID = {message.from_user.id}')
		db.db.commit()

	if message.text == '🔴 Back':
		shit6(message)
		if db.get_snazad(message.from_user.id)[0][0] == 0: await bot.send_message(message.from_user.id, 'Main menu', reply_markup = eb.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 1:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 0 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'Main menu', reply_markup = eb.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 2:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'Where do we start?', reply_markup = eb.kategorii)

	if message.text == 'First courses':
		fal(message)
		await bot.send_message(message.from_user.id, 'Choose a dish:', reply_markup = eb.odinblydo)
	if message.text == 'Second courses':
		fal(message)
		await bot.send_message(message.from_user.id, 'Choose a dish:', reply_markup = eb.dwablydo)
	if message.text == 'Meat dishes':
		fal(message)
		await bot.send_message(message.from_user.id, 'Choose a dish:', reply_markup = eb.myasoblydo)
	if message.text == 'Salads':
		fal(message)
		await bot.send_message(message.from_user.id, 'Choose a dish:', reply_markup = eb.salats)
	if message.text == 'Drinks':
		fal(message)
		await bot.send_message(message.from_user.id, 'Choose a dish:', reply_markup = eb.napitki)

	if message.text == 'To send':
		await bot.send_message(message.from_user.id, 'Expect a response.', reply_markup=eb.glmenu)
		db.kur.execute(f"SELECT ID FROM VSE")
		row = db.kur.fetchall()
		db.db.commit()
		info = row
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], f'''A new order has been received!

Name • <b>{db.get_name(message.from_user.id)[0][0]}</b>
Language • <b>{cfg.lang[db.get_lang(message.from_user.id)[0][0]]}</b>
Number • <code>+{db.get_num(message.from_user.id)[0][0]}</code>
Location • <code>{db.get_loc1(message.from_user.id)[0][0]}, {db.get_loc2(message.from_user.id)[0][0]}</code>

Orders:

Beef soup • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
Mastava soup • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
Lagman dish • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

Fried Lagman • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
Manta ray dish • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
Dolma dish • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

Lamb in a tandoor • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
Chicken kebab • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
Tikka Boti • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
Meat kebab • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
Bread with chicken • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
Bread with meat • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
Bread with shish kebab • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
Tandoor chicken (HALF) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
Tandoor chicken (WHOLE) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
Super pilaf combo • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
Pilaf dish • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
Pilaf offer • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

Greek salad • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
Vinigret • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
Olivier • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

Morello Cherry • {db.get_zakaz22(message.from_user.id)[0][0]}
Limonade • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup =ab.fune(message.chat.id))
			except:
				pass

	if message.text == '🗑Into a basket':
		if db.get_szakaz(message.from_user.id)[0][0] == 1: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 2: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 3: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 4: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 5: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 6: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 7: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 8: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 9: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 10: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 11: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 12: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 13: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 14: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 15: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 17: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 18: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 19: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 20: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 21: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 22: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 23: await shit3(message)

	if message.text == 'Choose more': await bot.send_message(message.from_user.id, 'Select a category:', reply_markup = eb.kategorii)

	if message.text == 'Beef soup':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 1 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo1, caption = cfg.zakaz1poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Mastava soup':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 2 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo2, caption = cfg.zakaz2poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Lagman dish':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 3 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo3, caption = cfg.zakaz3poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Fried Lagman':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 4 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo4, caption = cfg.zakaz4poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Manta ray dish':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 5 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo5, caption = cfg.zakaz5poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Dolma dish':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 6 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo6, caption = cfg.zakaz6poe, reply_markup = ibtn.keyboarde)
	#
	if message.text == 'Lamb in a tandoor':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 7 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo7, caption = cfg.zakaz7poe, reply_markup = ibtn.keyboarde)
	
	if message.text == 'Chicken kebab':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 8 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo8, caption = cfg.zakaz8poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Tikka Boti':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 9 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo9, caption = cfg.zakaz9por, reply_markup = ibtn.keyboarde)

	if message.text == 'Meat kebab':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 10 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo10, caption = cfg.zakaz10poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Bread with chicken':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 11 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo11, caption = cfg.zakaz11poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Bread with meat':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 12 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo12, caption = cfg.zakaz12poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Bread with shish kebab':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 13 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo13, caption = cfg.zakaz13poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Tandoor chicken (HALF)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 14 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo14, caption = cfg.zakaz14poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Tandoor chicken (WHOLE)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 15 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo15, caption = cfg.zakaz15poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Super pilaf combo':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 16 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo16, caption = cfg.zakaz16poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Pilaf dish':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 17 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo17, caption = cfg.zakaz17poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Pilaf offer':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 18 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo18, caption = cfg.zakaz18poe, reply_markup = ibtn.keyboarde)
	#
	if message.text == 'Greek':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 19 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo19, caption = cfg.zakaz19poe, reply_markup = ibtn.keyboarde)

	if message.text == 'Vinaigrette':
		await vina(message)

	if message.text == 'Olivier':
		await oliv(message)

	if message.text == 'Limonade':
		await Limonade(message)

	#arab yazik
	if message.text == '🇦🇪 العربية':
		if db.user_langs(message.from_user.id)[0][0] == 1:
			await bot.send_message(message.from_user.id, 'لقد نجحت في تغيير اللغة', reply_markup=arb.glmenu)
			db.kur.execute(f"UPDATE Accounts SET Lang = 4 WHERE id={message.from_user.id}")
			db.kur.execute(f"UPDATE Accounts SET LangState = 0 WHERE id={message.from_user.id}")
		else: 
			await bot.send_message(message.from_user.id, 'ما هي المدينة التي تعيش فيها?\nالرجاء الاختيار', reply_markup=ab.gorod)
			db.kur.execute(f"UPDATE Accounts SET Lang = 4 WHERE id={message.from_user.id}")
		db.db.commit()

	if message.text == '🛍 لأجل': await bot.send_message(message.from_user.id, 'من أين نبدأ?', reply_markup=arb.kategorii)

	if message.text == '🗑سلة':
		if not db.zakaz_get(message.from_user.id):
			await bot.send_message(message.from_user.id, 'ليس لديك أي أوامر', reply_markup=arb.glmenu)
		else:
			await shit5(message)

	if message.text == '⚙️ الإعدادات': await bot.send_message(message.from_user.id, 'حدد إجراء:', reply_markup=arb.settings)

	if message.text == '🇦🇪 تغيير اللغة':
		shit2(message)
		await bot.send_message(message.from_user.id, "اختر لغة:", reply_markup=ab.lang)

	if message.text == '🏙 تغيير المدينة': await bot.send_message(message.from_user.id, 'ما هي المدينة التي تعيش فيها?\nالرجاء الاختيار', reply_markup=ab.gorod)

	if message.text == '🔴 القائمة الرئيسية':
		await bot.send_message(message.from_user.id, 'القائمة الرئيسية', reply_markup=arb.glmenu)
		shit1(message)

	if message.text == '🔴 العودة':
		shit6(message)
		if db.get_snazad(message.from_user.id)[0][0] == 0: await bot.send_message(message.from_user.id, 'القائمة الرئيسية', reply_markup = arb.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 1:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 0 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'القائمة الرئيسية', reply_markup = arb.glmenu)
		if db.get_snazad(message.from_user.id)[0][0] == 2:
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'من أين نبدأ?', reply_markup = arb.kategorii)

	if message.text == 'الدورات الأولى':
		fal(message)
		await bot.send_message(message.from_user.id, 'اختيار طبق:', reply_markup = arb.odinblydo)
	if message.text == 'الدورات الثانية':
		fal(message)
		await bot.send_message(message.from_user.id, 'اختيار طبق:', reply_markup = arb.dwablydo)
	if message.text == 'أطباق اللحوم':
		fal(message)
		await bot.send_message(message.from_user.id, 'اختيار طبق:', reply_markup = arb.myasoblydo)
	if message.text == 'السلطات':
		fal(message)
		await bot.send_message(message.from_user.id, 'اختيار طبق:', reply_markup = arb.salats)
	if message.text == 'المشروبات':
		fal(message)
		await bot.send_message(message.from_user.id, 'اختيار طبق:', reply_markup = arb.napitki)

	if message.text == 'إرسال':
		await bot.send_message(message.from_user.id, 'توقع ردا.', reply_markup=arb.glmenu)
		db.kur.execute(f"SELECT ID FROM VSE")
		row = db.kur.fetchall()
		db.db.commit()
		info = row
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], f'''تم استلام طلب جديد!

الاسم • <b>{db.get_name(message.from_user.id)[0][0]}</b>
اللغة • <b>{cfg.lang[db.get_lang(message.from_user.id)[0][0]]}</b>
العدد • <code>+{db.get_num(message.from_user.id)[0][0]}</code>
الموقع • <code>{db.get_loc1(message.from_user.id)[0][0]}, {db.get_loc2(message.from_user.id)[0][0]}</code>

الطلبات:

حساء لحم البقر • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
حساء ماستافا • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
طبق لاجمان • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

فرايد لاجمان • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
طبق مانتا راي • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
طبق دولما • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

خروف في التندور • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
كباب الدجاج • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
تكا بوتي • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
كباب لحم • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
الخبز مع الدجاج • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
خبز باللحم • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
خبز مع يوقاب • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
دجاج التندور (نصف) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
دجاج التندور (كامل) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
سوبر بيلاف كومبو • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
طبق بيلاف • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
عرض بيلاف • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

سلطة يونانية • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
صلصة الخل • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
أوليفييه • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

موريلو الكرز • {db.get_zakaz22(message.from_user.id)[0][0]}
عصير الليمون • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup =ab.funar(message.chat.id))
			except:
				pass

	if message.text == 'إزالة':
		await bot.send_message(message.from_user.id, 'لقد قمت بحذفها بنجاح..', reply_markup = arb.glmenu)
		db.kur.execute(f'DELETE FROM Zakaz WHERE ID = {message.from_user.id}')
		db.db.commit()

	if message.text == "🗑 في سلة":
		if db.get_szakaz(message.from_user.id)[0][0] == 1: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 2: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 3: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 4: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 5: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 6: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 7: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 8: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 9: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 10: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 11: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 12: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 13: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 14: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 15: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 16: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 17: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 18: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 19: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 20: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 21: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 22: await shit3(message)
		if db.get_szakaz(message.from_user.id)[0][0] == 23: await shit3(message)

	if message.text == 'حساء لحم البقر':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 1 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo1, caption = cfg.zakaz1poar, reply_markup = ibtn.keyboardar)

	if message.text == 'حساء ماستافا':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 2 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo2, caption = cfg.zakaz2poar, reply_markup = ibtn.keyboardar)

	if message.text == 'طبق لاجمان':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 3 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo3, caption = cfg.zakaz3poar, reply_markup = ibtn.keyboardar)

	if message.text == 'فرايد لاجمان':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 4 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo4, caption = cfg.zakaz4poar, reply_markup = ibtn.keyboardar)

	if message.text == 'طبق مانتا راي':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 5 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo5, caption = cfg.zakaz5poar, reply_markup = ibtn.keyboardar)

	if message.text == 'طبق دولما':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 6 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo6, caption = cfg.zakaz6poar, reply_markup = ibtn.keyboardar)
	#
	if message.text == 'خروف في التندور':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 7 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo7, caption = cfg.zakaz7poar, reply_markup = ibtn.keyboardar)
	
	if message.text == 'كباب الدجاج':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 8 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo8, caption = cfg.zakaz8poar, reply_markup = ibtn.keyboardar)

	if message.text == 'تكا بوتي':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 9 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo9, caption = cfg.zakaz9por, reply_markup = ibtn.keyboardar)

	if message.text == 'كباب لحم':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 10 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo10, caption = cfg.zakaz10poar, reply_markup = ibtn.keyboardar)

	if message.text == 'الخبز مع الدجاج':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 11 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo11, caption = cfg.zakaz11por, reply_markup = ibtn.keyboardar)

	if message.text == 'خبز باللحم':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 12 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo12, caption = cfg.zakaz12poar, reply_markup = ibtn.keyboardar)

	if message.text == 'خبز مع يوقاب':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 13 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo13, caption = cfg.zakaz13poar, reply_markup = ibtn.keyboardar)

	if message.text == 'دجاج التندور (نصف)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 14 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo14, caption = cfg.zakaz14poar, reply_markup = ibtn.keyboardar)

	if message.text == 'دجاج التندور (كامل)':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 15 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo15, caption = cfg.zakaz15poar, reply_markup = ibtn.keyboardar)

	if message.text == 'سوبر بيلاف كومبو':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 16 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo16, caption = cfg.zakaz16poar, reply_markup = ibtn.keyboardar)

	if message.text == 'طبق بيلاف':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 17 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo17, caption = cfg.zakaz17poar, reply_markup = ibtn.keyboardar)

	if message.text == 'عرض بيلاف':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 18 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo18, caption = cfg.zakaz18poar, reply_markup = ibtn.keyboardar)
	#
	if message.text == 'اليونانية':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 19 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo19, caption = cfg.zakaz19por, reply_markup = ibtn.keyboardar)

	if message.text == 'صلصة الخل':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 20 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo20, caption = cfg.zakaz20poar, reply_markup = ibtn.keyboardar)

	if message.text == 'أوليفييه':
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 21 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo21, caption = cfg.zakaz21poar, reply_markup = ibtn.keyboardar)

	#
	if message.text == 'موريلو الكرز':
		await Morello(message)

	if message.text == 'عصير الليمون':
		await Limonade(message)
	
@dp.message_handler(state = cfg.getkolvo.kolvo)
async def getkolvoall(message : types.Message, state:FSMContext):
	await state.update_data(kolvo=message.text)
	data = await state.get_data()
	kolvo = data.get('kolvo')
	if not message.text in cfg.kolvos:
		if db.get_lang(message.from_user.id)[0][0] == 1: await message.answer('Ошибка!\nНеверный символ или большое число.')
		if db.get_lang(message.from_user.id)[0][0] == 2: await message.answer("Xato!\n Noto'g'ri belgi yoki katta raqam.")
		if db.get_lang(message.from_user.id)[0][0] == 3: await message.answer('Error!\n Incorrect sign or large number.')
		if db.get_lang(message.from_user.id)[0][0] == 4: await message.answer('خطأ!\n علامة غير صحيحة أو عدد كبير.')
	else:
		if kolvo == '🔴 Назад':
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, 'Выберите котегорию:', reply_markup = rb.kategorii)
			await state.finish()
		elif kolvo == '🔴 Orqaga':
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, "Toifani tanlang", reply_markup = ub.kategorii)
			await state.finish()
		elif kolvo == '🔴 Back':
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, "Select a Category", reply_markup = eb.kategorii)
			await state.finish()
		elif kolvo == '🔴 أورقاغا':
			db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
			db.db.commit()
			await bot.send_message(message.from_user.id, "حدد فئة", reply_markup = arb.kategorii)
			await state.finish()
		else:
			if db.get_szakaz(message.from_user.id)[0][0] == 1:
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz1(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz1 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 2:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz2(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz2 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 3:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz3(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz3 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 4:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz4(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz4 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 5:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz5(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz5 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 6:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz6(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz6 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 7:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz7(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz7 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 8:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz8(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz8 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 9:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz9(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz9 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 10:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz10(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz10 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 11:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz11(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz11 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 12:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz12(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz12 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 13:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz13(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz13 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 14:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz14(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz14 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 15:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz15(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz15 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 16:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz16(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz16 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 17:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz17(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz17 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 18:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz18(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz18 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 19:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz19(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz19 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 20:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz20(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz20 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 21:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz21(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz21 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 22:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo}, 0)")
					await shit7(message, state)
				else:
					if db.get_zakaz22(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz22 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

			if db.get_szakaz(message.from_user.id)[0][0] == 23:	
				db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
				if not db.get_zakazer(message.from_user.id):
					db.kur.execute(f"INSERT INTO Zakaz VALUES ({message.from_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {kolvo})")
					await shit7(message, state)
				else:
					if db.get_zakaz23(message.from_user.id)[0][0] > 0:
						await shit8(message)
					else:
						await shit7(message, state)
						db.kur.execute(f"UPDATE Zakaz SET zakaz23 = {kolvo} WHERE id={message.from_user.id}")
				db.db.commit()

@dp.message_handler(content_types=['contact'])
async def contact(message):
   	if message.contact.user_id != message.from_user.id:
   		if db.get_lang(message.from_user.id)[0][0] == 1: await message.reply("Отправьте свой контакт!")
   		if db.get_lang(message.from_user.id)[0][0] == 2: await message.reply("Kontaktingizni yuboring!")
   		if db.get_lang(message.from_user.id)[0][0] == 3: await message.reply("Send your contact!")
   		if db.get_lang(message.from_user.id)[0][0] == 4: await message.reply("إرسال جهة الاتصال الخاصة بك!")
   	else:
   		if db.get_lang(message.from_user.id)[0][0] == 1: await bot.send_message(message.from_user.id, 'Отправте геолокацию', reply_markup = rb.lol2)
   		if db.get_lang(message.from_user.id)[0][0] == 2: await bot.send_message(message.from_user.id, 'Geolokatsiyani yuborish', reply_markup = ub.lol2)
   		if db.get_lang(message.from_user.id)[0][0] == 3: await bot.send_message(message.from_user.id, 'Send geolocation', reply_markup = eb.lol2)
   		if db.get_lang(message.from_user.id)[0][0] == 4: await bot.send_message(message.from_user.id, 'إرسال الموقع الجغرافي', reply_markup = arb.lol2)
   		db.kur.execute(f"UPDATE Accounts SET Nomer = {message.contact.phone_number} WHERE id={message.from_user.id}")
   		db.db.commit()

@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    db.kur.execute(f"UPDATE Accounts SET Latitude = {message.location.latitude} WHERE id={message.from_user.id}")
    db.kur.execute(f"UPDATE Accounts SET Longitude = {message.location.longitude} WHERE id={message.from_user.id}")
    db.db.commit()
    if db.get_lang(message.from_user.id)[0][0] == 1: await bot.send_message(message.from_user.id, 'Готово!', reply_markup = rb.glmenu)
    if db.get_lang(message.from_user.id)[0][0] == 2: await bot.send_message(message.from_user.id, 'Tayyor!', reply_markup = ub.glmenu)
    if db.get_lang(message.from_user.id)[0][0] == 3: await bot.send_message(message.from_user.id, 'Done!', reply_markup = eb.glmenu)
    if db.get_lang(message.from_user.id)[0][0] == 4: await bot.send_message(message.from_user.id, 'تم!', reply_markup = arb.glmenu)

@dp.callback_query_handler(lambda call: True)
async def cal(call, state: FSMContext):
	if 'ansr' in call.data:
		await call.message.answer('🖊*Введи ответ:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item.set()
		a = call.data.index('-ansr')
		ids = call.data[:a]
		await state.update_data(uid=ids)
		await call.answer()
	if 'ansu' in call.data:
		await call.message.answer('🖊*Javobni kiriting:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item.set()
		a = call.data.index('-ansu')
		ids = call.data[:a]
		await state.update_data(uid=ids)
		await call.answer()
	if 'anse' in call.data:
		await call.message.answer('🖊*Enter the answer:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item.set()
		a = call.data.index('-anse')
		ids = call.data[:a]
		await state.update_data(uid=ids)
		await call.answer()
	if 'ansar' in call.data:
		await call.message.answer('🖊*أدخل الجواب:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item.set()
		a = call.data.index('-ansar')
		ids = call.data[:a]
		await state.update_data(uid=ids)
		await call.answer()
	elif 'otkazr' in call.data:
		z = call.data.index('-otkazr')
		idd = call.data[:z]
		await call.message.answer('🖊*Введи причину:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item2.set()
		await state.update_data(iss=idd)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await call.answer()
	elif 'otkazu' in call.data:
		z = call.data.index('-otkazu')
		idd = call.data[:z]
		await call.message.answer('🖊*Sababini kiriting:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item2.set()
		await state.update_data(iss=idd)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await call.answer()
	elif 'otkaze' in call.data:
		z = call.data.index('-otkaze')
		idd = call.data[:z]
		await call.message.answer('🖊*Sababini kiriting:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item2.set()
		await state.update_data(iss=idd)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await call.answer()
	elif 'otkazar' in call.data:
		z = call.data.index('-otkazar')
		idd = call.data[:z]
		await call.message.answer('🖊*أدخل السبب:*', parse_mode= 'Markdown')
		await cfg.getkolvo.item2.set()
		await state.update_data(iss=idd)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await call.answer()
		
@dp.message_handler(state = cfg.getkolvo.adds)
async def ads(message: types.Message, state: FSMContext):
	if not db.asd(message.text):
		await message.reply('id successfully added')
		db.kur.execute(f"INSERT INTO VSE VALUES ({message.text})")
		await state.finish()
		db.db.commit()
	else:
		await message.reply('such an ID already exists')
		await state.finish()

@dp.message_handler(state = cfg.getkolvo.dadds)
async def ads(message: types.Message, state: FSMContext):
	if not db.asd(message.text):
		await message.reply('there is no such id')
		await state.finish()
	else:
		await message.reply('id successfully deleted')
		db.kur.execute(f'DELETE FROM VSE WHERE ID = {message.text}')
		db.db.commit()
		await state.finish()

@dp.message_handler(state=cfg.getkolvo.item)
async def proc(message: types.Message, state: FSMContext):
	if db.get_lang(message.from_user.id)[0][0] == 1: await message.answer('✅*Сообщение отправлено!*', parse_mode= 'Markdown', reply_markup=rb.glmenu)
	if db.get_lang(message.from_user.id)[0][0] == 2: await message.answer('✅*Xabar yuborildi!*', parse_mode= 'Markdown', reply_markup=ub.glmenu)
	if db.get_lang(message.from_user.id)[0][0] == 3: await message.answer('✅*The message has been sent!*', parse_mode= 'Markdown', reply_markup=eb.glmenu)
	if db.get_lang(message.from_user.id)[0][0] == 4: await message.answer('✅*تم إرسال الرسالة!*', parse_mode= 'Markdown', reply_markup=arb.glmenu)
	data = await state.get_data()
	id = data.get("uid")
	await state.finish()
	if db.get_lang(message.from_user.id)[0][0] == 1: await bot.send_message(id, f'<b>☂️Вам поступил ответ!</b>\n\n<b>📝Текст:</b> {message.text}', parse_mode= 'HTML')
	if db.get_lang(message.from_user.id)[0][0] == 2: await bot.send_message(id, f'<b>Sizga javob keldi!</b>\n\n<b>📝Matn:</b> {message.text}', parse_mode= 'HTML')
	if db.get_lang(message.from_user.id)[0][0] == 3: await bot.send_message(id, f'<b>☂️You have received an answer!</b>\n\n<b>📝Text:</b> {message.text}', parse_mode= 'HTML')
	if db.get_lang(message.from_user.id)[0][0] == 4: await bot.send_message(id, f'<b>☂️لقد تلقيت إجابة!</b>\n\n<b>📝النص:</b> {message.text}', parse_mode= 'HTML')

@dp.message_handler(state=cfg.getkolvo.item2)
async def proc(message: types.Message, state: FSMContext):
	if db.get_lang(message.from_user.id)[0][0] == 1: await message.answer('✅*Сообщение отправлено!*', parse_mode= 'Markdown', reply_markup=rb.glmenu)
	if db.get_lang(message.from_user.id)[0][0] == 2: await message.answer('✅*Xabar yuborildi!*', parse_mode= 'Markdown', reply_markup=ub.glmenu)
	if db.get_lang(message.from_user.id)[0][0] == 3: await message.answer('✅*The message has been sent!*', parse_mode= 'Markdown', reply_markup=eb.glmenu)
	if db.get_lang(message.from_user.id)[0][0] == 4: await message.answer('✅*تم إرسال الرسالة!*', parse_mode= 'Markdown', reply_markup=arb.glmenu)
	data = await state.get_data()
	id = data.get("iss")
	await state.finish()
	db.kur.execute('DELETE FROM Zakaz WHERE ID = (id);')
	db.db.commit()
	if db.get_lang(message.from_user.id)[0][0] == 1: await bot.send_message(id, f'<b>☂️Вам поступил ответ!</b>\n\n<b>📝Текст:</b> {message.text}', parse_mode= 'HTML')
	if db.get_lang(message.from_user.id)[0][0] == 2: await bot.send_message(id, f'<b>Sizga javob keldi!</b>\n\n<b>📝Matn:</b> {message.text}', parse_mode= 'HTML')
	if db.get_lang(message.from_user.id)[0][0] == 3: await bot.send_message(id, f'<b>☂️You have received an answer!</b>\n\n<b>📝Text:</b> {message.text}', parse_mode= 'HTML')
	if db.get_lang(message.from_user.id)[0][0] == 4: await bot.send_message(id, f'<b>☂️لقد تلقيت إجابة!</b>\n\n<b>📝النص:</b> {message.text}', parse_mode= 'HTML')

def shit1(message):
	db.kur.execute(f"UPDATE Accounts SET LangState = 0 WHERE id={message.from_user.id}")
	db.db.commit()

def shit2(message):
	db.kur.execute(f"UPDATE Accounts SET LangState = 1 WHERE id={message.from_user.id}")
	db.db.commit()

async def shit3(message):
	if db.get_lang(message.from_user.id)[0][0] == 1:
		await bot.send_message(message.from_user.id, 'Выбирите количество:', reply_markup = rb.setkolvo)
		await cfg.getkolvo.kolvo.set()

	if db.get_lang(message.from_user.id)[0][0] == 2:
		await bot.send_message(message.from_user.id, 'Miqdorni tanlang:', reply_markup = ub.setkolvo)
		await cfg.getkolvo.kolvo.set()
	if db.get_lang(message.from_user.id)[0][0] == 3:
		await bot.send_message(message.from_user.id, 'Select the quantity:', reply_markup = eb.setkolvo)
		await cfg.getkolvo.kolvo.set()

	if db.get_lang(message.from_user.id)[0][0] == 4:
		await bot.send_message(message.from_user.id, 'حدد الكمية:', reply_markup = arb.setkolvo)
		await cfg.getkolvo.kolvo.set()

async def shit4(message):
	if db.get_lang(message.from_user.id)[0][0] == 1: await bot.send_message(message.from_user.id, 'Отправте контакт.', reply_markup=rb.lol)
	if db.get_lang(message.from_user.id)[0][0] == 2: await bot.send_message(message.from_user.id, "Kontaktni yuboring", reply_markup=ub.lol)
	if db.get_lang(message.from_user.id)[0][0] == 3: await bot.send_message(message.from_user.id, 'Send a contact.', reply_markup=eb.lol)
	if db.get_lang(message.from_user.id)[0][0] == 4: await bot.send_message(message.from_user.id, 'إرسال جهة اتصال.', reply_markup=arb.lol)

async def shit5(message):
	if db.get_lang(message.from_user.id)[0][0] == 1: await message.answer(f'''
Суп из говядины • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
Суп из маставы • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
Блюдо из лагмана • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

Лагман жареный • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
Блюдо из мантов • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
Блюдо из долмы • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

Ягнёнок в тандыре • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
Куриный шашлык • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
Тикка Боти • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
Мясной шашлык • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
Хлеб с цыпленком • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
Хлеб с мясом • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
Хлеб с кекабом • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
Тандырная курица (ПОЛОВИНА) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
Тандырная курица (ЦЕЛАЯ) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
Супер плов комбо • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
Блюдо из плова • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
Предложение плова • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

Греческий салат • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
Винигрет • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
Оливье • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

Morello Cherry • {db.get_zakaz22(message.from_user.id)[0][0]}
Limonade • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup = ibtn.keyboardr2)

	if db.get_lang(message.from_user.id)[0][0] == 2: await message.answer(f'''
Mol go'shti sho'rvasi • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
Mastava sho'rva • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
Lagman taomlari • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

Lagman qovurilgan • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
Manti taomlari • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
Dolma taom • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

Tandirda qo'zichoq • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
Tovuq kaboblari • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
Tikka Boti • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
Go'shtli shish • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
Tovuq bilan non • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
Go'sht bilan non • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
Yokab bilan non • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
Tandir Tovuqi (yarim) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
Tandir Tovuqi (butun) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
Super palov kombinati • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
Palovdan tayyorlangan taom • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
Palov taklifi • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

Yunon salatasi • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
Vinaigrette • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
Olivier • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

Morello Cherry • {db.get_zakaz22(message.from_user.id)[0][0]}
Limonade • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup = ibtn.keyboardu2)

	if db.get_lang(message.from_user.id)[0][0] == 3: await message.answer(f'''
Beef soup • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
Mastava soup • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
Lagman dish • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

Fried Lagman • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
Manta ray dish • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
Dolma dish • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

Lamb in a tandoor • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
Chicken kebab • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
Tikka Boti • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
Meat kebab • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
Bread with chicken • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
Bread with meat • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
Bread with shish kebab • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
Tandoor chicken (HALF) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
Tandoor chicken (WHOLE) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
Super pilaf combo • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
Pilaf dish • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
Pilaf offer • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

Greek salad • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
Vinigret • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
Olivier • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

Morello Cherry • {db.get_zakaz22(message.from_user.id)[0][0]}
Limonade • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup = ibtn.keyboarde2)

	if db.get_lang(message.from_user.id)[0][0] == 4:
		await bot.send_message(cfg.admin, f'''
حساء لحم البقر • <b>{db.get_zakaz1(message.from_user.id)[0][0]}</b>
حساء ماستافا • <b>{db.get_zakaz2(message.from_user.id)[0][0]}</b>
طبق لاجمان • <b>{db.get_zakaz3(message.from_user.id)[0][0]}</b>

فرايد لاجمان • <b>{db.get_zakaz4(message.from_user.id)[0][0]}</b>
طبق مانتا راي • <b>{db.get_zakaz5(message.from_user.id)[0][0]}</b>
طبق دولما • <b>{db.get_zakaz6(message.from_user.id)[0][0]}</b>

خروف في التندور • <b>{db.get_zakaz7(message.from_user.id)[0][0]}</b>
كباب الدجاج • <b>{db.get_zakaz8(message.from_user.id)[0][0]}</b>
تكا بوتي • <b>{db.get_zakaz9(message.from_user.id)[0][0]}</b>
كباب لحم • <b>{db.get_zakaz10(message.from_user.id)[0][0]}</b>
الخبز مع الدجاج • <b>{db.get_zakaz11(message.from_user.id)[0][0]}</b>
خبز باللحم • <b>{db.get_zakaz12(message.from_user.id)[0][0]}</b>
خبز مع يوقاب • <b>{db.get_zakaz13(message.from_user.id)[0][0]}</b>
دجاج التندور (نصف) • <b>{db.get_zakaz14(message.from_user.id)[0][0]}</b>
دجاج التندور (كامل) • <b>{db.get_zakaz15(message.from_user.id)[0][0]}</b>
سوبر بيلاف كومبو • <b>{db.get_zakaz16(message.from_user.id)[0][0]}</b>
طبق بيلاف • <b>{db.get_zakaz17(message.from_user.id)[0][0]}</b>
عرض بيلاف • <b>{db.get_zakaz18(message.from_user.id)[0][0]}</b>

سلطة يونانية • <b>{db.get_zakaz19(message.from_user.id)[0][0]}</b>
صلصة الخل • <b>{db.get_zakaz20(message.from_user.id)[0][0]}</b>
أوليفييه • <b>{db.get_zakaz21(message.from_user.id)[0][0]}</b>

موريلو الكرز • {db.get_zakaz22(message.from_user.id)[0][0]}
عصير الليمون • {db.get_zakaz23(message.from_user.id)[0][0]}
''', parse_mode = 'HTML', reply_markup = ibtn.keyboardar2)

def shit6(message):
	db.kur.execute(f"UPDATE Accounts SET StateZakaz = 0 WHERE id={message.from_user.id}")
	db.db.commit()

async def shit7(message, state : FSMContext):
	data = await state.get_data()
	kolvo = data.get('kolvo')
	if db.get_lang(message.from_user.id)[0][0] == 1:
		fal(message)
		await message.answer(f'Введённое количество: {kolvo}\n\nВаш заказ отправлен в корзину\nчтобы подтвердить заказ перейдите в корзину', reply_markup = rb.kategorii)
		await state.finish()

	if db.get_lang(message.from_user.id)[0][0] == 2:
		fal(message)
		await message.answer(f"Kiritilgan miqdor: {kolvo}\n\nBuyurtmangiz Savatga yuborildi buyurtmani tasdiqlash uchun Savatga o'ting", reply_markup = ub.kategorii)
		await state.finish()

	if db.get_lang(message.from_user.id)[0][0] == 3:
		fal(message)
		await message.answer(f'Entered quantity: {kolvo}\n\nYour order has been sent to the cart to confirm the order, go to the cart', reply_markup = eb.kategorii)
		await state.finish()

	if db.get_lang(message.from_user.id)[0][0] == 4:
		fal(message)
		await message.answer(f'الكمية المدخلة: {kolvo}\n\nتم إرسال طلبك إلى عربة التسوق لتأكيد الطلب ، انتقل إلى عربة التسوق', reply_markup = arb.kategorii)
		await state.finish()

async def shit8(message):
	if db.get_lang(message.from_user.id)[0][0] == 1: await message.answer('Вы уже выбрали, изменять заказ запрещено')
	if db.get_lang(message.from_user.id)[0][0] == 2: await message.answer("Siz allaqachon tanladingiz, buyurtmani o'zgartirish taqiqlanadi")
	if db.get_lang(message.from_user.id)[0][0] == 3: await message.answer('You have already chosen, it is forbidden to change the order')
	if db.get_lang(message.from_user.id)[0][0] == 4: await message.answer('لقد اخترت بالفعل ، يحظر تغيير الترتيب')

async def Limonade(message):
	if db.get_lang(message.from_user.id)[0][0] == 1:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 23 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz23por, reply_markup = ibtn.keyboardr)
	if db.get_lang(message.from_user.id)[0][0] == 2:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 23 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz23pou, reply_markup = ibtn.keyboardu)
	if db.get_lang(message.from_user.id)[0][0] == 3:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 23 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz23poe, reply_markup = ibtn.keyboarde)
	if db.get_lang(message.from_user.id)[0][0] == 4:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 23 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz23poar, reply_markup = ibtn.keyboardar)

async def Morello(message):
	if db.get_lang(message.from_user.id)[0][0] == 1:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 22 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz22por, reply_markup = ibtn.keyboardr)
	if db.get_lang(message.from_user.id)[0][0] == 2:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 22 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz22pou, reply_markup = ibtn.keyboardu)
	if db.get_lang(message.from_user.id)[0][0] == 3:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 22 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz22poe, reply_markup = ibtn.keyboarde)
	if db.get_lang(message.from_user.id)[0][0] == 4:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 22 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo22, caption = cfg.zakaz22poar, reply_markup = ibtn.keyboardar)

def fal(message):
	db.kur.execute(f"UPDATE Accounts SET SNAZAD = 1 WHERE id={message.from_user.id}")
	db.db.commit()

def fal2(message):
	db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
	db.db.commit()

async def oliv(message):
	if db.get_lang(message.from_user.id)[0][0] == 2:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 21 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo21, caption = cfg.zakaz21pou, reply_markup = ibtn.keyboardu)
	if db.get_lang(message.from_user.id)[0][0] == 3:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 21 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo21, caption = cfg.zakaz21poe, reply_markup = ibtn.keyboarde)

async def vina(message):
	if db.get_lang(message.from_user.id)[0][0] == 2:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 20 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo20, caption = cfg.zakaz20pou, reply_markup = ibtn.keyboardu)
	if db.get_lang(message.from_user.id)[0][0] == 3:
		db.kur.execute(f"UPDATE Accounts SET StateZakaz = 20 WHERE id={message.from_user.id}")
		db.kur.execute(f"UPDATE Accounts SET SNAZAD = 2 WHERE id={message.from_user.id}")
		db.db.commit()
		await bot.send_photo(chat_id=message.chat.id, photo=cfg.photo20, caption = cfg.zakaz20poe, reply_markup = ibtn.keyboarde)

if __name__ == '__main__': executor.start_polling(dp, skip_updates = True)