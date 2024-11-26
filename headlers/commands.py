from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app import bot
import yfinance as yf
from utils.database.request import add_symbol_db as asdb


router = Router()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Добро пожаловать, {message.from_user.first_name} !")

@router.message(Command("ticker"))
async def cmd_ticker(message: Message):
    await message.answer("Введите тикер акции")

@router.message()
async def receive_symbol(message: Message):
    try:
        symbol = yf.Ticker(message.text)
        symbolData = symbol.info
        shortName = symbolData['shortName']
        currentPrice = symbolData['currentPrice']
        data = f"""Названия акции: {shortName}\nТекущая цена: {currentPrice}
"""
        await bot.send_message(message.from_user.id, data)
    except:
        await message.answer("🙇‍♀️🙇‍♀️🙇‍♀️ Тикер акции не найден!")
    symbolName = symbolData['symbol']
    await asdb(message.from_user.id, symbolName, sheet_id=None)