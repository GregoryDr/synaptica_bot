import asyncio
import logging
from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
from aiogram.filters.command import Command

# Включаем логирование, чтоб не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token = "6595799419:AAEhizAtZ2W6LxWf6xSVS4jONyDNDJWw1lI")

# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cdm_start(message: types.Message):
    await message.answer("Hello Ann!")

# Запуск процесса полинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
