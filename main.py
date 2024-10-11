# coding:utf-8
from config import TOKEN,MONGODB,DATABASE,COLLECTION,COLLECTION2, COLLECTION3,admin_id, DEBUG, DEBUG_TOKEN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command,CommandObject
from aiogram.fsm.state import State,StatesGroup
from pymongo.mongo_client import MongoClient
from pymongo import MongoClient,DESCENDING
from aiogram.fsm.context import FSMContext
from aiogram import Bot,types,Dispatcher
import string
import logging
import asyncio
import random
import time
import sys
import proxy
import string
import math
import re
import hashlib
import json
from time import time
from hashlib import md5
from copy import deepcopy
from random import choice
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.command import Command, CommandStart
import keyboards
import requests
from urllib.parse import quote
import util

usecount = 0

c_proxy = {
    "http": "http://"+util.require_not_none(proxy.get_next_proxy_http())
}

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
if DEBUG:
    bot = Bot(token=DEBUG_TOKEN)
else:
    bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()

client = MongoClient(MONGODB)
database = client[DATABASE]
collection = database[COLLECTION]
promocol = database[COLLECTION2]
refcol = database[COLLECTION3]

class rasilka(StatesGroup):
    message = State()

@dp.message(Command("send_all"))
async def send_all(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if user_id in admin_id:
        await message.answer('Write a message for mailing')
        await state.set_state(rasilka.message)

@dp.message(rasilka.message)
async def handle_message_for_broadcast(message: types.Message, state: FSMContext):
    state_message = message
    user_id = message.from_user.id
    await state.clear()
    if user_id in admin_id:
        if DEBUG:
            ids = admin_id
        else:
            ids = [user['id'] for user in collection.find({}, {'id': 1, '_id': 0})]
        i = 0
        for user_id in ids:
            try:
                await state_message.copy_to(user_id, reply_markup=state_message.reply_markup)
                i += 1
            except:
                pass
        await message.reply(f"Отправил {i} пользователям")
    # await state.clear()

class SessionWait(StatesGroup):
    session = State()
    new_username = State()
    # choosing_food_size = State()

class Ref(StatesGroup):
    ref = State()

import binascii
import hashlib
import json
from time import time
from hashlib import md5
from copy import deepcopy
from random import choice


def hex_string(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = '0' + tmp_string
    return tmp_string


def RBIT(num):
    result = ''
    tmp_string = bin(num)[2:]
    while len(tmp_string) < 8:
        tmp_string = '0' + tmp_string
    for i in range(0, 8):
        result = result + tmp_string[7 - i]
    return int(result, 2)


def file_data(path):
    with open(path, 'rb') as f:
        result = f.read()
    return result


def reverse(num):
    tmp_string = hex(num)[2:]
    if len(tmp_string) < 2:
        tmp_string = '0' + tmp_string
    return int(tmp_string[1:] + tmp_string[:1], 16)


class XG:
    def __init__(self, debug):
        self.length = 0x14
        self.debug = debug
        self.hex_CE0 = [0x05, 0x00, 0x50, choice(range(0, 0xFF)), 0x47, 0x1e, 0x00, choice(range(0, 0xFF)) & 0xf0]

    def addr_BA8(self):
        tmp = ''
        hex_BA8 = []
        for i in range(0x0, 0x100):
            hex_BA8.append(i)
        for i in range(0, 0x100):
            if i == 0:
                A = 0
            elif tmp:
                A = tmp
            else:
                A = hex_BA8[i - 1]
            B = self.hex_CE0[i % 0x8]
            if A == 0x05:
                if i != 1:
                    if tmp != 0x05:
                        A = 0
            C = A + i + B
            while C >= 0x100:
                C = C - 0x100
            if C < i:
                tmp = C
            else:
                tmp = ''
            D = hex_BA8[C]
            hex_BA8[i] = D
        return hex_BA8

    def initial(self, debug, hex_BA8):
        tmp_add = []
        tmp_hex = deepcopy(hex_BA8)
        for i in range(self.length):
            A = debug[i]
            if not tmp_add:
                B = 0
            else:
                B = tmp_add[-1]
            C = hex_BA8[i + 1] + B
            while C >= 0x100:
                C = C - 0x100
            tmp_add.append(C)
            D = tmp_hex[C]
            tmp_hex[i + 1] = D
            E = D + D
            while E >= 0x100:
                E = E - 0x100
            F = tmp_hex[E]
            G = A ^ F
            debug[i] = G
        return debug

    def calculate(self, debug):
        for i in range(self.length):
            A = debug[i]
            B = reverse(A)
            C = debug[(i + 1) % self.length]
            D = B ^ C
            E = RBIT(D)
            F = E ^ self.length
            G = ~F
            while G < 0:
                G += 0x100000000
            H = int(hex(G)[-2:], 16)
            debug[i] = H
        return debug

    def main(self):
        result = ''
        for item in self.calculate(self.initial(self.debug, self.addr_BA8())):
            result = result + hex_string(item)

        return '8404{}{}{}{}{}'.format(hex_string(self.hex_CE0[7]), hex_string(self.hex_CE0[3]),
                                       hex_string(self.hex_CE0[1]), hex_string(self.hex_CE0[6]), result)


def X_Gorgon(param, data, cookie):
    gorgon = []
    ttime = time()
    Khronos = hex(int(ttime))[2:]
    url_md5 = md5(bytearray(param, 'utf-8')).hexdigest()
    for i in range(0, 4):
        gorgon.append(int(url_md5[2 * i: 2 * i + 2], 16))
    if data:
        if isinstance(data, str):
            data = data.encode(encoding='utf-8')
        data_md5 = md5(data).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(data_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    if cookie:
        cookie_md5 = md5(bytearray(cookie, 'utf-8')).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(cookie_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    gorgon = gorgon + [0x1, 0x1, 0x2, 0x4]
    for i in range(0, 4):
        gorgon.append(int(Khronos[2 * i: 2 * i + 2], 16))
    return {'X-Gorgon': XG(gorgon).main(), 'X-Khronos': str(int(ttime))}


def run(param="", stub="", cookie=""):
    gorgon = []
    ttime = time()
    Khronos = hex(int(ttime))[2:]
    url_md5 = md5(bytearray(param, 'utf-8')).hexdigest()
    for i in range(0, 4):
        gorgon.append(int(url_md5[2 * i: 2 * i + 2], 16))
    if stub:
        data_md5 = stub
        for i in range(0, 4):
            gorgon.append(int(data_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    if cookie:
        cookie_md5 = md5(bytearray(cookie, 'utf-8')).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(cookie_md5[2 * i: 2 * i + 2], 16))
    else:
        for i in range(0, 4):
            gorgon.append(0x0)
    gorgon = gorgon + [0x1, 0x1, 0x2, 0x4]
    for i in range(0, 4):
        gorgon.append(int(Khronos[2 * i: 2 * i + 2], 16))
    return {'X-Gorgon': XG(gorgon).main(), 'X-Khronos': str(int(ttime))}


def get_stub(data):
    if isinstance(data, dict):
        data = json.dumps(data)

    if isinstance(data, str):
        data = data.encode(encoding='utf-8')
    if data == None or data == "" or len(data) == 0:
        return "00000000000000000000000000000000"

    m = hashlib.md5()
    m.update(data)
    res = m.hexdigest()
    res = res.upper()
    return res


def get_profile(session_id, device_id, iid):
    """Retrieve the current TikTok username for a given session, device, and iid."""
    try:
        
        url = f"https://api.tiktokv.com/passport/account/info/v2/?id=kaa&version_code=34.0.0&language=en&app_name=lite&app_version=34.0.0&carrier_region=SA&device_id=7256623439258404357&tz_offset=10800&mcc_mnc=42001&locale=en&sys_region=SA&aid=473824&screen_width=1284&os_api=18&ac=WIFI&os_version=17.3&app_language=en&tz_name=Asia/Riyadh&carrier_region1=SA&build_number=340002&device_platform=iphone&iid=7353686754157692689&device_type=iPhone13,4"
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": f"sessionid={session_id}",
            "sdk-version": "2",
            "user-agent": "com.zhiliaoapp.musically/432424234 (Linux; U; Android 5; en; fewfwdw; Build/PI;tt-ok/3.12.13.1)",
  
        }
        
        response = requests.get(url, headers=headers, cookies={"sessionid": session_id})
        return response.json()["data"]["username"]
    except Exception as e:
        return "None"


def check_is_changed(last_username, session_id, device_id, iid):
    """Check if the username has been changed in the TikTok profile."""
    return get_profile(session_id, device_id, iid) != last_username


def change_username(session_id, device_id, iid, last_username, new_username):
    """Attempt to change a TikTok username."""
    data = f"aid=364225&unique_id={quote(new_username)}"
    parm = f"aid=364225&residence=&device_id={device_id}&version_name=1.1.0&os_version=17.4.1&iid={iid}&app_name=tiktok_snail&locale=en&ac=4G&sys_region=SA&version_code=1.1.0&channel=App%20Store&op_region=SA&os_api=18&device_brand=iPad&idfv=16045E07-1ED5-4350-9318-77A1469C0B89&device_platform=iPad&device_type=iPad13,4&carrier_region1=&tz_name=Asia/Riyadh&account_region=sa&build_number=11005&tz_offset=10800&app_language=en&carrier_region=&current_region=&aid=364225&mcc_mnc=&screen_width=1284&uoo=1&content_language=&language=en&cdid=B75649A607DA449D8FF2ADE97E0BC3F1&openudid=7b053588b18d61b89c891592139b68d918b44933&app_version=1.1.0"
    
        
    sig = run(parm, md5(data.encode("utf-8")).hexdigest() if data else None,None)  
    url = f"https://api.tiktokv.com/aweme/v1/commit/user/?{parm}"
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Whee 1.1.0 rv:11005 (iPad; iOS 17.4.1; en_SA@calendar=gregorian) Cronet",


        "Cookie": f"sessionid={session_id}",
    }
    headers.update(sig)
    response = requests.post(url, data=data, headers=headers)
    result = response.text
    if "unique_id" in result :
        if(check_is_changed(last_username, session_id, device_id, iid)):
            return True
        else:
            return "Failed to change username: " + str(result)
    else:
        return "Failed to change username: " + str(result)
@dp.message(CommandStart(
    deep_link=True,
    magic=F.args.regexp(re.compile(r'ref_(.+)'))
))
async def cmd_start_ref(
        message: types.Message,
        command: CommandObject
):
    
        # if refobj[""]
    await message.answer("Приветсвую тебя в боте для создания запрещённых ников в TikTok!\n⚠️Если сменить ник не получается попробуйте поставить регион на египет⚠️\nДля получения бесплатных смен ника заходите в каналы авторов", reply_markup=keyboards.main_kb())
    user_id = message.from_user.id
    user_name = message.from_user.username
    user = {
        "id" : user_id,
        "Name" : user_name,
        "Used" : False
    }
    if collection.find_one({"id": user_id}) is None:
        ref = command.args.split("_")[1]
        print("Ref:", ref)
        refobj = refcol.find_one({"name": ref})
        if refobj is not None:
            refuses = int(refobj["used"]) + 1
            boninc = 0
            if refuses % 5 == 0:
                boninc = 1
            refcol.update_one({"name": ref}, {"$inc": {"used": 1}}) # Use a dictionary here
            refcol.update_one({"name": ref}, {"$inc": {"bonuses": boninc}})
        collection.insert_one(user)

@dp.message(CommandStart(deep_link=True,magic=F.args.regexp(re.compile(r'promo_(.+)'))))
async def cmd_start_promo(message: types.Message,command: CommandObject):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user = {
        "id" : user_id,
        "Name" : user_name,
        "Used" : False
    }
    if collection.find_one({"id": user_id}) is None:
        collection.insert_one(user)
    promo = command.args.split("_")[1]
    msg = await message.answer(f"Активирую...")
    pr = promocol.find_one({"promo": promo})
    user = collection.find_one({"id": user_id})
    if pr is None:
        await msg.answer("Промокод не найден")
        return
    uses = pr["uses"]
    usedusers = pr["activated"]
    if len(usedusers) >= uses:
        await msg.edit_text("Промокод уже использован максимальное кол-во раз!")
        return
    if message.from_user.id in usedusers:
        await msg.edit_text("Вы уже использовали этот промокод!")
        return
    if user["Used"] == True:
        collection.update_one({"id": message.from_user.id}, {"$set": {"Used": False}})
        promocol.update_one({'promo': promo}, {'$push': {'activated': message.from_user.id}})
        await msg.answer_sticker("https://raw.githubusercontent.com/TelegramBots/book/master/src/docs/sticker-fred.webp")
        await msg.delete()
        await message.answer("✅Вы успешно активировали промокод\nТеперь вы опять можете сменить ник")
    else:
        await msg.edit_text("❌У вас уже есть бесплатная смена ника")
    
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Приветсвую тебя в боте для создания запрещённых ников в TikTok!\n⚠️Если сменить ник не получается попробуйте поставить регион на египет⚠️\nДля получения бесплатных смен ника заходите в каналы авторов", reply_markup=keyboards.main_kb())
    user_id = message.from_user.id
    user_name = message.from_user.username
    user = {
        "id" : user_id,
        "Name" : user_name,
        "Used" : False
    }
    if collection.find_one({"id": user_id}) is None:
        collection.insert_one(user)

@dp.message(Command("genpromo"))
async def genpromo(message: types.Message):
    user_id = message.from_user.id
    if user_id in admin_id:
        promo = message.text.split()[1]
        uses = int(message.text.split()[2])
        botusename = await bot.get_me()

        promocol.insert_one({"promo": promo, "uses": uses, "activated":[]})
        
        
        await message.answer(f"💡 Новый промокод!\n🍒 Кол-во активаций: {uses}\nt.me/{botusename.username}?start=promo_{promo}")

@dp.message(Command("ref"))
async def refsys(message: types.Message):
    refdata = refcol.find_one({"creator": message.from_user.id})
    if refdata is None:
        await message.answer("У вас нет своей реферальной ссылки!", reply_markup=keyboards.ref_kb())
        return
    botusename = await bot.get_me()
    await message.answer(f"🌶️ {refdata['name']}\nПереходов: {refdata['used']}\n\nРеферальный баланс: {refdata['bonuses']}\nВаша реферальная ссылка: t.me/{botusename.username}?start=ref_{refdata['name']}\n\nНе покупайте новую смену ника если у вас уже есть одна смена ника", reply_markup=keyboards.ref_asort_kb())

@dp.callback_query(F.data == "createref")
async def createref(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("Введите текст ссылки (только англ. буквы и цифры)\nПример: strnq (ссылка будет выглядить так: t.me/runick_bot?start=ref_strnq)")
    await state.set_state(Ref.ref)
    await callback.answer()

@dp.message(Ref.ref)
async def createref_f(message: types.Message, state: FSMContext):
    ref_name = message.text.replace(" ", "_")
    if refcol.find_one({"name": ref_name}) != None:
        await message.answer("Ссылка уже занята! Введите название ещё раз")
        return
    refcol.insert_one({
        "name": ref_name,
        "creator": message.from_user.id,
        "used": 0,
        "bonuses": 0
    })
    botusename = await bot.get_me()
    await message.answer(f"Ссылка успешно создана!\nt.me/{botusename.username}?start=ref_{ref_name}")
    await state.clear()

prices = {"1": 1, "2": 5, "3": 100}

@dp.message(Command("id"))
async def refsys(message: types.Message):
    user_id = message.from_user.id
    if user_id in admin_id:
        id = int(message.text.split()[1])
        await message.answer(f"tg://user?id={id}")
    else:
        await message.answer("❌У вас нету доступа")
    

@dp.callback_query(F.data.contains("buy:"))
async def buy_handler(callback: types.CallbackQuery):
    refdata = refcol.find_one({"creator": callback.from_user.id})
    if refdata is None:
        await callback.message.answer("У вас нет своей реферальной ссылки!", reply_markup=keyboards.ref_kb())
        return
    tovar = callback.data.split(":")[1]
    price = prices[tovar]

    if refdata["bonuses"] < price:
        await callback.message.answer("У вас недостаточно средств!")
        return
    
    match tovar:
        case "1":
            user = collection.find_one({"id": callback.from_user.id})
            if not user["Used"]:
                await callback.message.answer("У вас уже есть смена ника!")
                # refcol.update_one({"creator": callback.from_user.id}, {"$inc": {"bonuses": price}})
                await callback.answer()
                return
            collection.update_one({"id": callback.from_user.id},{"$set": {"Used": False}})
            
            # await callback.message.answer("Успешная покупка!")
        case "2":
            botusename = await bot.get_me()

            promo = f"{refdata['name']}-{''.join([random.choice(string.ascii_lowercase+string.digits) for i in range(6)])}"

            if promocol.find_one({"name": promo}) is not None:
                await callback.message.answer("Ошибка попробуй ещё раз! (Шанс это увидить 0.0000000459%)")
                return

            promocol.insert_one({"promo": promo, "uses": 5, "activated":[]})
            
            await callback.message.answer(f"💡 Новый промокод!\n🍒 Кол-во активаций: 5\nt.me/{botusename.username}?start=promo_{promo}")
        case "3":
            await callback.message.answer("Перешлите это сообщение @squirrel882 и ожидайте")
            
    refcol.update_one({"creator": callback.from_user.id}, {"$inc": {"bonuses": -price}})
    await callback.message.answer("Успешная покупка!")
    await callback.answer()

@dp.callback_query(F.data == "begin")
async def begin(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Выбери вариант изменения ника:", reply_markup=keyboards.begin_kb())

@dp.callback_query(F.data.contains("change:"))
async def changenick(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()
    # photo = open("123.png", "rb")
    if (callback.data.split(":")[1] == "1"):
        await callback.message.answer_video(types.FSInputFile("123.mp4"), caption="❇️ Скиньте свой session id!\n[Сайт для конвертации куки в session id](https://belkaspace.buzz/)\n[Способ если не выдает неверный сид](https://t.me/c/2234743135/164)", parse_mode="Markdown")
        await state.set_state(SessionWait.session)
    # photo.close()

    # ты пидарас
# ало блять микро включи

@dp.message(SessionWait.session)
async def changeusername(message: types.Message, state: FSMContext):
    if(len(message.text)<30):
        await message.answer("Слишком короткий session id! Попробуйте ещё раз")
        return
    await state.update_data(session=message.text)
    await message.answer("Введите новый ник (без @)")
    await state.set_state(SessionWait.new_username)


@dp.message(SessionWait.new_username)
async def changeusername_final(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = collection.find_one({"id": user_id})
    if(user["Used"]==True):
        await message.answer("Вы уже использовали свою смену ника!\nПолучайте новые смены следя за каналами ниже", reply_markup=keyboards.main_kb())
        await state.clear()
        return
    global c_proxy, usecount
    if(usecount>6):
        newproxy = proxy.get_next_proxy_http()
        if newproxy != None:
            c_proxy = {
                "http": "http://"+newproxy
            }
        usecount = 0
    # await message.answer("Введите новый ник (без @)")
    state_data = await state.get_data()
    # await message.reply()
    session_id = state_data.get("session", "IDK")
    new_username = message.text
    await state.clear()
    device_id = str(random.randint(777777788, 999999999999))
    iid = str(random.randint(777777788, 999999999999))
    print(session_id,new_username)

    user = get_profile(session_id, device_id, iid)
    if user != "None":
        await message.answer(f"Ваш текущий ник: {user}")
        result = change_username(session_id, device_id, iid, user, new_username)
        if result == True:
            await message.answer(f"Ваш новый ник {new_username}")
            usecount +=1
            collection.update_one({"id": user_id}, {"$set": {"Used": True}})
        else:
            await message.answer(f"Ошибка смены ника {result}")
    else:
        await message.answer(f"Неверный sid или другая ошибка")
            
# @dp.message(Command("leaderboards"))
# async def leaderboards(message: types.Message):
#     top_users = refcol.find().sort("used", DESCENDING).limit(10)
#     leaderboard = "Топ 10 реферальных ссылок:\n\n"

#     for i, user in enumerate(top_users, start=1):
#         username = user["name"]
#         balance = user["used"]
#         leaderboard += f"{i}. {username}: {balance}\n"

#     await bot.send_message(message.from_user.id, leaderboard)

@dp.message(Command("leaderboards"))
async def leaderboards(message: types.Message):
    # Получаем топ 10 пользователей
    top_users = refcol.find().sort("used", DESCENDING).limit(10)
    
    # Считаем общее количество использованных реферальных ссылок
    total_referrals = refcol.aggregate([{"$group": {"_id": None, "total": {"$sum": "$used"}}}])
    total_referrals_count = total_referrals.next().get("total", 0)  # получаем сумму рефералов или 0, если пусто

    # Формируем текст для отправки
    leaderboard = f"Общее количество рефералов: {total_referrals_count}\n\n"
    leaderboard += "Топ 10 реферальных ссылок:\n\n"

    for i, user in enumerate(top_users, start=1):
        username = user["name"]
        balance = user["used"]
        leaderboard += f"{i}. {username}: {balance}\n"

    await bot.send_message(message.from_user.id, leaderboard)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())