import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from utils.database import init_db
from commands.handlers import handle_commands, handle_text
from config import DA_TOKEN

bot = Bot(DA_TOKEN)
dp = Dispatcher()

async def main():
    await init_db()
    dp.message.register(
        handle_commands,
        Command(commands=["start", "help", "lowercase", "lower", "uppercase", "upper", "capitalize"])
    )
    dp.message.register(handle_text, F.text & ~F.text.startswith("/"))
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())