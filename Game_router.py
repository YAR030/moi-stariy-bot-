from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
import lvls
import Keyboards
from States import states, game_states
from aiogram.fsm.context import FSMContext
from db import Database
from Game_logika import Game
router = Router()
db = Database('Db_users.db')

move_dict = {'up': [0, -1],
             'douw': [0, 1],
             'left': [-1, 0],
             'right': [1, 0]}


@router.message(F.text == 'Играть в человечка который умеет двигать кубики')
async def run_lvl1(message: types.Message, state: FSMContext):
    await message.answer(text='Выберите уровень', reply_markup=Keyboards.lvl_menu)
    await state.set_state(game_states.change_lvl)


@router.message(game_states.change_lvl, F.text == '1 уровень')
async def run_lvl1(message: types.Message,state: FSMContext):
    db.set_pole(message.from_user.id, lvls.lvl_1().pole_str)
    await message.answer(text='1 уровень',reply_markup=Keyboards.lvl_in_game_menu)
    await message.answer(text=Game(lvls.lvl_1().pole_str).print_tg(), reply_markup=Keyboards.my_game_menu)
    await state.set_state(game_states.lvl_1)


@router.message(game_states.change_lvl, F.text == '2 уровень')
async def run_lvl2(message: types.Message,state: FSMContext):
    db.set_pole(message.from_user.id, lvls.lvl_2().pole_str)
    await message.answer(text='2 уровень',reply_markup=Keyboards.lvl_in_game_menu)
    await message.answer(text=Game(lvls.lvl_2().pole_str, lvls.lvl_2().pole_size).print_tg(), reply_markup=Keyboards.my_game_menu)
    await state.set_state(game_states.lvl_2)


@router.message(F.text == 'Назад')
async def restart_lvl(message: types.Message, state: FSMContext):
    await message.answer(text='Выберите уровень', reply_markup=Keyboards.lvl_menu)
    await state.set_state(game_states.change_lvl)


@router.callback_query(game_states.lvl_1)
async def run_lvl_1(callback: types.CallbackQuery, state: FSMContext):
    await move_lvl(callback, state, lvls.lvl_1().pole_size)

@router.callback_query(game_states.lvl_2)
async def run_lvl_2(callback: types.CallbackQuery, state: FSMContext):
    await move_lvl(callback, state, lvls.lvl_2().pole_size)




async def move_lvl(callback, state, lvl_size):
    pole = Game(db.output_pole(callback.from_user.id), lvl_size).move(move_dict[callback.data])
    if Game(pole, lvl_size).lvl_complited():
        await callback.message.answer(text=Game(pole, lvl_size).print_tg(), reply_markup=Keyboards.lvl_menu)
        await callback.message.answer(text='Вы прошли уровень', reply_markup=Keyboards.lvl_menu)
        await state.set_state(game_states.change_lvl)

    else:
        try:
            await callback.message.edit_text(text=Game(pole, lvl_size).print_tg(), reply_markup=Keyboards.my_game_menu)
            db.set_pole(callback.from_user.id, pole)
        except:
            pass