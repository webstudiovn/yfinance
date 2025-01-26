from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.database.model.user_class import User

def generate_inline_keyboard(users):
    bulder = InlineKeyboardBuilder()
    if users is None or not users:
        return InlineKeyboardMarkup(inline_keyboard=[])
    for user in users:
        if isinstance(user, User):
            button_text = f"{user.symbol}"
            callback_data = f"ticker_{user.symbol}"
            bulder.add(
                InlineKeyboardButton(
                    text=button_text,
                    callback_data=callback_data
                )
            )
    return bulder.as_markup()