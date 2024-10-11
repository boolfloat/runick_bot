from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

def main_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="♦️ Начать пользоваться", callback_data="begin")
    )
    builder.row(types.InlineKeyboardButton(
        text="🐿️ Дупло Белки",
        url="https://t.me/+VWlXwUUOzR8wZTY1")
    )
    builder.row(types.InlineKeyboardButton(
        text="🩸 strnq's lounge",
        url="tg://resolve?domain=bystrnq")
    )
    builder.row(types.InlineKeyboardButton(
        text="Все вопросы сюда",
        url="https://t.me/+VWlXwUUOzR8wZTY1"
    ))

    return builder.as_markup()


def begin_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="*️⃣ Session ID", callback_data="change:1")
    )

    return builder.as_markup()

def ref_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="▶️ Создать", callback_data="createref")
    )

    return builder.as_markup()

def ref_asort_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="🍉 Купить смену ника (1 реф валюта)", callback_data="buy:1")
    )
    builder.row(types.InlineKeyboardButton(
        text="🥳 Промокод на 5 активаций (5 реф валют)", callback_data="buy:2")
    )
    builder.row(types.InlineKeyboardButton(
        text="🥨 Безлимит в боте (100 реф валют)", callback_data="buy:3")
    )

    return builder.as_markup()