import sqlite3

db = sqlite3.connect("db/bot.db",check_same_thread=False)
kur = db.cursor()

def creater():
    kur.execute("CREATE TABLE IF NOT EXISTS Accounts (ID INTEGER, Name TEXT, Nomer INTEGER, Latitude INTEGER, Longitude INTEGER,  Lang INTEGER, Gorod INTEGER, LangState INTEGER, StateZakaz INTEGER, SNAZAD INTEGER)")
    kur.execute("CREATE TABLE IF NOT EXISTS Zakaz (ID INTEGER, zakaz1 INTEGER, zakaz2 INTEGER, zakaz3 INTEGER, zakaz4 INTEGER, zakaz5 INTEGER, zakaz6 INTEGER, zakaz7 INTEGER, zakaz8 INTEGER, zakaz9 INTEGER, zakaz10 INTEGER, zakaz11 INTEGER, zakaz12 INTEGER, zakaz13 INTEGER, zakaz14 INTEGER, zakaz15 INTEGER, zakaz16 INTEGER, zakaz17 INTEGER, zakaz18 INTEGER, zakaz19 INTEGER, zakaz20 INTEGER, zakaz21 INTEGER, zakaz22 INTEGER, zakaz23 INTEGER)")
    db.commit()

def get_snazad(id):
    kur.execute(f"SELECT SNAZAD FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def user_exists(id):
    kur.execute(f"SELECT ID FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def user_state(id):
    kur.execute(f"SELECT State FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def user_langs(id):
    kur.execute(f"SELECT LangState FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def zakaz_get(id):
    kur.execute(f"SELECT ID FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_lang(id):
    kur.execute(f"SELECT Lang FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def get_szakaz(id):
    kur.execute(f"SELECT StateZakaz FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def get_name(id):
    kur.execute(f"SELECT Name FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def get_loc1(id):
    kur.execute(f"SELECT Latitude FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def get_loc2(id):
    kur.execute(f"SELECT Longitude FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def get_num(id):
    kur.execute(f"SELECT Nomer FROM Accounts WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakazer(id):
    kur.execute(f"SELECT ID FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz1(id):
    kur.execute(f"SELECT zakaz1 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz2(id):
    kur.execute(f"SELECT zakaz2 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz3(id):
    kur.execute(f"SELECT zakaz3 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz4(id):
    kur.execute(f"SELECT zakaz4 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz5(id):
    kur.execute(f"SELECT zakaz5 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz6(id):
    kur.execute(f"SELECT zakaz6 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz7(id):
    kur.execute(f"SELECT zakaz7 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz8(id):
    kur.execute(f"SELECT zakaz8 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz9(id):
    kur.execute(f"SELECT zakaz9 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz10(id):
    kur.execute(f"SELECT zakaz10 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz11(id):
    kur.execute(f"SELECT zakaz11 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz12(id):
    kur.execute(f"SELECT zakaz12 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz13(id):
    kur.execute(f"SELECT zakaz13 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz14(id):
    kur.execute(f"SELECT zakaz14 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz15(id):
    kur.execute(f"SELECT zakaz15 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz16(id):
    kur.execute(f"SELECT zakaz16 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz17(id):
    kur.execute(f"SELECT zakaz17 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz18(id):
    kur.execute(f"SELECT zakaz18 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz19(id):
    kur.execute(f"SELECT zakaz19 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz20(id):
    kur.execute(f"SELECT zakaz20 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz21(id):
    kur.execute(f"SELECT zakaz21 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz22(id):
    kur.execute(f"SELECT zakaz22 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def get_zakaz23(id):
    kur.execute(f"SELECT zakaz23 FROM Zakaz WHERE id=(?)",(id,))
    return kur.fetchall()

def asd(id):
    kur.execute(f"SELECT ID FROM VSE WHERE id=(?)",(id,))
    return kur.fetchall()