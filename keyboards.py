from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton




start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)



menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
            [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)


product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text='Саподилла', callback_data="product_buying")],
            [InlineKeyboardButton(text='Чомпу', callback_data="product_buying")],
            [InlineKeyboardButton(text='Аки', callback_data="product_buying")],
            [InlineKeyboardButton(text='Амбарелла', callback_data="product_buying")]
    ]
)




