from aiogram import Dispatcher
import logging
import bot_info
import asyncio
import main
import Game_router
import settings
dp = Dispatcher()

dp.include_routers(main.router,
                   settings.router,
                   Game_router.router)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot_info.bot)


if __name__ == "__main__":
    asyncio.run(main())

