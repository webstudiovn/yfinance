import json
import pprint
from aiogram.utils.markdown import text
import asyncio
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app import bot
#from aiogram.types.callback_query import CallbackQuery
# user imports
#from utils.database.request import add_user, select_users
#from utils.keyboard.inline_keyboard import generate_inline_keyboard
from utils.bourses import get_moex_data, get_spb_data

router = Router()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Добро пожаловать, {message.from_user.first_name} !")

@router.message(Command("ticker"))
async def cmd_ticker(message: Message):
    await message.answer("Введите тикер акции в 4-х или 5-ти значном формате (БУКВЫ) с Московской биржи")

@router.message(Command("editgoogle"))
async def edit_google(message: Message):
    await message.answer("Введите свой ID Google таблицы")


#@router.message(Command("mytickers"))
#async def symbols_list(message: Message):
 #   user = await select_users()
  #  symbols_info = generate_inline_keyboard(user)
   # await message.answer("Список тикеров", reply_markup=symbols_info)

@router.message()
async def get_data_bourse(message: Message):
    symbol = message.text.upper()
    await message.answer("Ищем информацию об тикере...")

    moex_data = await get_moex_data(symbol)
    spb_data = await get_spb_data(symbol)

    info_dict = list()
    
    max_retries = 2
    for _ in range(max_retries):
        if moex_data:
            # Первый вызов для получения данных
            moex_result = await get_moex_data(moex_data)
            
            # Второй вызов для сохранения результатов
            if moex_result is not None:
                info_dict.append(moex_result)

        elif spb_data:
            # Первый вызов для получения данных
            spb_result = await get_spb_data(spb_data)
            
            # Второй вызов для сохранения результатов
            if spb_result is not None:
                info_dict.append(spb_result)
        
        if not (moex_data or spb_data):
            await message.answer("Не удалось получить данные ни от MOEX, ни от SPB.")
            await asyncio.sleep(640)
        
    if not info_dict:
        info_string = "К сожалению, не удалось найти информацию об этом тикере."
    else:
        info_string = "\n".join([f"{k}: {v}" for k, v in info_dict.items()])
    # Формирование ответа
    messageSend = text(f"Информация о тикере:\n\n{info_string}")
    print(info_dict)

    print(messageSend)

    # Отправка сообщения в бота
    await bot.send_message(message.from_user.id, messageSend)
