from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

lvl_in_game_kb = [[KeyboardButton(text='Назад')]]
lvl_kb = [
    [
        KeyboardButton(text='1 уровень')
    ],
    [
        KeyboardButton(text='2 уровень')
    ],
    [
        KeyboardButton(text='Назад➡️')
    ]
]

help_kb = [
    [
        KeyboardButton(text='Сделать запрос'),
        KeyboardButton(text='Поиграть в кликер')
    ],
    [
        KeyboardButton(text='Играть в человечка который умеет двигать кубики')
    ],
    [
        KeyboardButton(text='⚙️Настройки⚙️')
    ]
]

my_game_but = [
    [
        InlineKeyboardButton(text='Вверх', callback_data='up')
    ],
    [
        InlineKeyboardButton(text='Влево', callback_data='left'),
        InlineKeyboardButton(text='Вправо', callback_data='right')
    ],
    [
        InlineKeyboardButton(text='Вниз', callback_data='douw')
    ]
]

game_but = [
    [
        InlineKeyboardButton(text='Играть',
                             web_app=WebAppInfo(url='https://yar030.github.io/Clicker_Test/')),
    ]
]

settings_but = [
    [
        KeyboardButton(text='Настройки показа страницы'),
        KeyboardButton(text='Настройки поиска')
    ],
    [
        KeyboardButton(text='Назад➡️')
    ]
]
settings_search_but = [
    [
        KeyboardButton(text='Расширенный поиск'),
        KeyboardButton(text='Обычной поиск')
    ],
    [
        KeyboardButton(text='Назад➡️')
    ]
]
settings_page_but = [
    [
        KeyboardButton(text='Первые 10 предложений'),
        KeyboardButton(text='Первое предложение')
    ],
    [
        KeyboardButton(text='Назад➡️')
    ]
]



help_menu = ReplyKeyboardMarkup(keyboard=help_kb, resize_keyboard=True)
game_menu = InlineKeyboardMarkup(inline_keyboard=game_but)
q_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад➡️')]], resize_keyboard=True)
lvl_menu = ReplyKeyboardMarkup(keyboard=lvl_kb, resize_keyboard=True)
my_game_menu = InlineKeyboardMarkup(inline_keyboard=my_game_but)
lvl_in_game_menu = ReplyKeyboardMarkup(keyboard=lvl_in_game_kb, resize_keyboard=True)
settings_menu = ReplyKeyboardMarkup(keyboard=settings_but, resize_keyboard=True)
settings_search_menu = ReplyKeyboardMarkup(keyboard=settings_search_but, resize_keyboard=True)
settings_page_menu = ReplyKeyboardMarkup(keyboard=settings_page_but, resize_keyboard=True)