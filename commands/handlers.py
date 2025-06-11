import aiosqlite
from aiogram import types
from aiogram.types import Message
from utils.database import fetch_user_mode
from config import CUSTOM_ID, SPECIAL_MSG, DB_PATH

async def handle_commands(message: types.Message):
    user_id = str(message.from_user.id)
    user_cmd = message.text[1:].lower()
    
    mode = await first_process_command(user_cmd, message, user_id)
    if mode is not None:
        await update_user_data(user_id, message.from_user.username, mode)

async def first_process_command(command: str, message: types.Message, user_id: str) -> int | None:
    match command:
        case "help":
            await message.answer("This bot can transform your messages to lowercase, UPPERCASE, or Capitalised. Use /lowercase, /uppercase, or /capitalize to set your preferred mode.")
        case "start":
            welcome_message = (
                SPECIAL_MSG if user_id == CUSTOM_ID 
                else "Welcome! Send me a message and I'll change its case. Use /help for more info."
            )
            await message.answer(welcome_message)
        case "lowercase" | "lower":
            await message.answer("Mode set to lowercase. Send me a message!")
            return 1000
        case "uppercase" | "upper":
            await message.answer("Mode set to UPPERCASE. Send me a message!")
            return 2000
        case "capitalize":
            await message.answer("Mode set to Capitalised. Send me a message!")
            return 3000
        case _:
            await message.answer("Invalid command. Please try again or use /help.")
            return None

async def update_user_data(user_id: str, username: str, selected_mode: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO people_using_the_bot (id, username, mode)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET username=excluded.username, mode=excluded.mode
        ''', (user_id, username, selected_mode))
        await db.commit()

async def handle_text(message: Message):
    user_id = str(message.from_user.id)
    mode = await fetch_user_mode(user_id)

    if mode == 1000:
        text = message.text.lower()
    elif mode == 2000:
        text = message.text.upper()
    elif mode == 3000:
        text = message.text.capitalize()
    else:
        text = "Choose a mode with /lowercase, /uppercase or /capitalise!"

    await message.answer(text)