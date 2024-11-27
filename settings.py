from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
import Keyboards
from States import states
from aiogram.fsm.context import FSMContext
from db import Database, Database_settings
router = Router()
db_settings = Database_settings('Db_users.db')

@router.message(F.text == '⚙️Настройки⚙️')
async def settings_start(message: types.Message):
    await message.answer(text='Выберите что хотите настроить', reply_markup=Keyboards.settings_menu)


@router.message(F.text == 'Настройки поиска')
async def setting_page(message:types.Message):
    await message.answer(text='При расширенном поиске вам юудет предложено несоклько вариантов поиска', reply_markup=Keyboards.settings_search_menu)


@router.message(F.text == 'Настройки показа страницы')
async def setting_page(message:types.Message):
    await message.answer(text='Выберите что вам будет показываться при ответе на запрос', reply_markup=Keyboards.settings_page_menu)




@router.message(F.text == 'Расширенный поиск')
async def setting_page(message: types.Message):
    await message.answer(text='Настройки успешно применины',reply_markup=Keyboards.help_menu)
    db_settings.set_mode_search(message.from_user.id, 1)

@router.message(F.text == 'Обычной поиск')
async def setting_page(message: types.Message):
    await message.answer(text='Настройки успешно применины',reply_markup=Keyboards.help_menu)
    db_settings.set_mode_search(message.from_user.id, 0)



@router.message(F.text == 'Первые 10 предложений')
async def setting_page(message: types.Message):
    await message.answer(text='Настройки успешно применины',reply_markup=Keyboards.help_menu)
    db_settings.set_mode_page(message.from_user.id, 1)

@router.message(F.text == 'Первое предложение')
async def setting_page(message: types.Message):
    await message.answer(text='Настройки успешно применины',reply_markup=Keyboards.help_menu)
    db_settings.set_mode_page(message.from_user.id, 0)