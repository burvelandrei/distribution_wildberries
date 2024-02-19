import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from handlers import user_handlers, other_handlers


logger = logging.getLogger(__name__)

async def main():


    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s'
    )


    logger.info('Starting Bot')




    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()


    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)



    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())