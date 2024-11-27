from aiogram.fsm.state import StatesGroup, State


class states (StatesGroup):
    q = State()
    q_a = State()

class game_states (StatesGroup):
    change_lvl = State()
    lvl_1 = State()
    lvl_2 = State()