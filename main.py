from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, InlineKeyboardMarkup

import wiki_v2
import Keyboards
from States import states
from aiogram.fsm.context import FSMContext
from db import Database, Database_settings
router = Router()
db = Database('Db_users.db')
db_settings = Database_settings('Db_users.db')

@router.message(CommandStart())
async def comand_start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    if not db_settings.user_exists(message.from_user.id):
        db_settings.add_all(message.from_user.id, 0, 0)

    await message.answer(text=f'Привет {message.from_user.full_name}', reply_markup=ReplyKeyboardRemove())


@router.message(Command("help"))
async def command_help(message: types.Message, state: FSMContext):
    await message.answer(text="Можно в 2 игры, или сделать запрос", reply_markup=Keyboards.help_menu)
    await state.clear()

@router.message(F.text == 'Назад➡️')
async def question(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text='Можно в 2 игры, или сделать запрос', reply_markup=Keyboards.help_menu)


@router.message(F.text == 'Поиграть в кликер')
async def play_game(message: types.Message, state: FSMContext):
    await state.set_state(states.q)
    await message.answer(text='Кликер (не поддерживается на ПК)', reply_markup=Keyboards.game_menu)


@router.message(F.text == 'Сделать запрос')
async def wiki_q(message: types.Message, state: FSMContext):

        await state.set_state(states.q)
        await message.answer(text='Спрашивайте', reply_markup=Keyboards.q_menu)



@router.message(states.q)
async def question_start(message: types.Message, state:FSMContext):
    if db_settings.give_mode_search(message.from_user.id) == 1:
        try:
            mark_up = InlineKeyboardMarkup(inline_keyboard=wiki_v2.wiki_choise(message.text))
            await message.answer(text='Выбирайте', reply_markup=mark_up)
            await state.set_state(states.q_a)
        except:
            await message.answer(text='Ничего не удалось найти')
    else:
        try:
            await message.answer(text=wiki_v2.wiki_search_a(message.text, db_settings.give_mode_page(message.from_user.id)))

        except:
            await message.answer(text='Ничего не удалось найти')


@router.callback_query(states.q_a)
async def question_a(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text=wiki_v2.wiki_search_a(callback.data, db_settings.give_mode_page(callback.from_user.id)))
    await state.set_state(states.q)