import aiosqlite
import os
from config import DB_PATH

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS people_using_the_bot (
                id TEXT UNIQUE,
                username TEXT,
                mode INTEGER,
                PRIMARY KEY (id)
            )
        ''')
        await db.commit()

async def update_db(user_id: str, username: str, selected_mode: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
            INSERT INTO people_using_the_bot (id, username, mode)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET username=excluded.username, mode=excluded.mode
        ''', (user_id, username, selected_mode))
        await db.commit()

async def fetch_user_mode(user_id: str) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT mode FROM people_using_the_bot WHERE id = ?", (user_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else 1000  # Default to lowercase mode if user not found