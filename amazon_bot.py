from re import M
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery, Message

bot = Bot(token="5129599162:AAHmqlzOnWbMifFJ2USAW3OXqhlt2hGlE9o", parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class sms12(StatesGroup):
    sms_text = State()

class sms11(StatesGroup):
    sms_text = State()

class sms10(StatesGroup):
    sms_text = State()

class sms9(StatesGroup):
    sms_text = State()

class sms8(StatesGroup):
    sms_text = State()

class sms7(StatesGroup):
    sms_text = State()

class sms6(StatesGroup):
    sms_text = State()

class sms5(StatesGroup):
    sms_text = State()

class sms4(StatesGroup):
    sms_text = State()

class sms3(StatesGroup):
    sms_text = State()

class sms2(StatesGroup):
    sms_text = State()

xxx = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📋 Оператор", callback_data="oper"),
            InlineKeyboardButton(text="📋 Техпродажи", callback_data="tex")
        ],

        [
            InlineKeyboardButton(text="📋 Бот", callback_data="bbb"),
            InlineKeyboardButton(text="📋 Hudra", callback_data="hudra")
        ],

        [
            InlineKeyboardButton(text="📋 Работа", callback_data="rab"),
            InlineKeyboardButton(text="📋 Работа WhatsApp", callback_data="whatsApp")
        ],

        [
            InlineKeyboardButton(text="📋 Резерв", callback_data="rezerv"),
            InlineKeyboardButton(text="📋 Legal", callback_data="leg")
        ],

        [
            InlineKeyboardButton(text="📋 Отзывы", callback_data="otz")
        ],

        [
            InlineKeyboardButton(text="📋 Фон сайта", callback_data="fon"),
            InlineKeyboardButton(text="📋 Логотип", callback_data="logot")        
        ],

        [
            InlineKeyboardButton(text="CКАЧАТЬ ШАБЛОН", callback_data="shab")
        ]
    ]
)

with open ('index.html', 'r') as f:
  old_data = f.readlines()
  tt = old_data[518]
  tat = tt.split('"')
  otziv = tat[7]
  tt1 = old_data[505]
  tat1 = tt1.split('"')
  legal = tat1[7]
  tt2 = old_data[497]
  tat2 = tt2.split('"')
  rez = tat2[7]
  tt3 = old_data[481]
  tat3 = tt3.split('"')
  wc = tat3[7]
  tt4 = old_data[474]
  tat4 = tt4.split('"')
  rabota = tat4[7]
  tt5 = old_data[459]
  tat5 = tt5.split('"')
  gidra = tat5[7]
  tt6 = old_data[452]
  tat6 = tt6.split('"')
  bbboot = tat6[7]
  tt7 = old_data[439]
  tat7 = tt7.split('"')
  texx = tat7[1]
  tt8 = old_data[430]
  tat8 = tt8.split('"')
  oer = tat8[7]


@dp.message_handler(commands=['start'])
async def start(message: Message):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await message.answer(
      f"<b>Пример сайта онлаин тут: </b>\n\n"
      f"http://81.90.181.16:8080\n"
      f"<b>Сейчас Установлены такие контакты: </b>\n\n"
      f"<b>📋 Оператор:</b>  <code>{oer}</code>\n"
      f"<b>📋 Техпродажи:</b> <code>{texx}</code>\n"
      f"<b>📋 Бот:</b>  <code>{bbboot}</code>\n"
      f"<b>📋 Hudra:</b>  <code>{gidra}</code>\n"
      f"<b>📋 Работа:</b> <code>{rabota}</code>\n"
      f"<b>📋 Работа WhatsApp:</b>  <code>{wc}</code>\n"
      f"<b>📋 Резерв:</b> <code>{rez}</code>\n"
      f"<b>📋 Legal:</b>  <code>{legal}</code>\n"
      f"<b>📋 Отзывы:</b> <code>{otziv}</code>\n\n"
      f"<b>Изменение контактов</b>", reply_markup=xxx)




@dp.callback_query_handler(text="shab", state="*")
async def logot(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    f = 'index.html'
    await bot.send_document(chat_id, open(f, 'rb'))



@dp.callback_query_handler(text="logot", state="*")
async def logot(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[413]
      tat = tt.split('"')
      zc = tat[29][22:-2]
    await call.message.answer(
      f"<b>Сейчас установлен {zc}</b>\n\n"
      f"<b>Введи сылку на изображение в таком формате http://image.jpg </b>"
                                 )
    await sms12.sms_text.set()

    @dp.message_handler(state=sms12.sms_text)
    async def logot(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        print(sms[-3:])
        if sms[-3:] == "jpg":
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(zc, sms)
          
          with open ('index.html', 'w') as f:
            f.write(new_data)

          await call.message.answer(
            f"<b>Логотип успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)
        else:
          await call.message.answer("Не верный формат")

@dp.callback_query_handler(text="fon", state="*")
async def fon(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[378]
      tat = tt.split('"')
      zc = tat[1][22:-2]
    await call.message.answer(
      f"<b>Сейчас установлен {zc}</b>\n\n"
      f"<b>Введи сылку на изображение в таком формате http://image.jpg </b>"
                                 )
    await sms11.sms_text.set()

    @dp.message_handler(state=sms11.sms_text)
    async def otz(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        print(sms[-3:])
        if sms[-3:] == "jpg":
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(zc, sms)
          
          with open ('index.html', 'w') as f:
            f.write(new_data)
          await call.message.answer(
            f"<b>Фон успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)



@dp.callback_query_handler(text="otz", state="*")
async def otz(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]


    await call.message.answer(
      f"<b>Сейчас установлен {otziv}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>"
                                 )
    await sms10.sms_text.set()


    @dp.message_handler(state=sms10.sms_text)
    async def otz(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(otziv, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)


        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)

@dp.callback_query_handler(text="leg", state="*")
async def leg(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]

    await call.message.answer(
      f"<b>Сейчас установлен {legal}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>"
                                 )
    await sms9.sms_text.set()


    @dp.message_handler(state=sms9.sms_text)
    async def leg(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(legal, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)


@dp.callback_query_handler(text="rezerv", state="*")
async def rezerv(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {rez}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>",
                                 )
    await sms8.sms_text.set()


    @dp.message_handler(state=sms8.sms_text)
    async def rezerv(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(rez, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)

@dp.callback_query_handler(text="whatsApp", state="*")
async def whatsApp(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {wc}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>",
                                 )
    await sms7.sms_text.set()


    @dp.message_handler(state=sms7.sms_text)
    async def whatsApp(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(wc, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)


@dp.callback_query_handler(text="rab", state="*")
async def rab(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {rabota}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>",
                                 )
    await sms6.sms_text.set()


    @dp.message_handler(state=sms6.sms_text)
    async def rab(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(rabota, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)



@dp.callback_query_handler(text="hudra", state="*")
async def hudra(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {gidra}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>",
                                 )
    await sms5.sms_text.set()


    @dp.message_handler(state=sms5.sms_text)
    async def hudra(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(gidra, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)


@dp.callback_query_handler(text="bbb", state="*")
async def bbb(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {bbboot}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>",
                                 )
    await sms4.sms_text.set()


    @dp.message_handler(state=sms4.sms_text)
    async def bbb(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(bbboot, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)


@dp.callback_query_handler(text="tex", state="*")
async def texp(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {texx}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>",
                                 )
    await sms3.sms_text.set()


    @dp.message_handler(state=sms3.sms_text)
    async def texp(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(texx, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)



@dp.callback_query_handler(text="oper", state="*")
async def oper(call: CallbackQuery, state: FSMContext):
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]


    await call.message.answer(
      f"<b>Сейчас установлен {oer}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>",
                                 )
    await sms2.sms_text.set()


    @dp.message_handler(state=sms2.sms_text)
    async def operator(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(oer, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)

        await call.message.answer(
            f"<b>Контакт успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://81.90.181.16:8080\n"
            , reply_markup=xxx)

if __name__ == "__main__":
    executor.start_polling(dp)
