# The_case_bot

A borderline useless Telegram bot written in Python using [Aiogram 3](https://docs.aiogram.dev/en/latest/). This bot transforms your messages into lowercase, UPPERCASE, or Capitalised text.  
Mainly a personal playground for bot development, but hey, maybe you’ll find it fun too.

---

## ✨ Features

- 🔤 Convert messages to lowercase, UPPERCASE, or Capitalised.
- ⚡ Simple commands to switch modes:
  - `/lowercase` or `/lower` — transform messages to lowercase
  - `/uppercase` or `/upper` — transform messages to uppercase
  - `/capitalise` — transform messages to capitalised form
- 👤 Custom welcome message for a specified user ID.
- 💾 Stores user preferences and usernames in an SQLite database (auto-created, no setup needed).
- 💤 Asynchronous, fast, and snarky.

---

## 🛠️ Setup

1. **Clone the repo:**
   ```sh
   git clone https://github.com/Alessandrx204/The_case_bot
   cd The_case_bot
   ```

2. **Configure your bot:**
   - Copy your Telegram bot token.
   - Edit `thecasebot.conf`:
     ```ini
     [bot]
     DA_TOKEN = YOUR_TELEGRAM_BOT_TOKEN

     [custom]
     CUSTOM_ID = YOUR_TELEGRAM_USER_ID   # (optional, for custom welcome)
     SPECIAL_MSG = Your custom welcome message!  # (optional)
     ```

3. **Install dependencies:**
   ```sh
   poetry install
   ```

4. **Run the bot:**
   ```sh
   poetry run main.py
   ```

   The database will be created automatically in the `database/` folder.

---

## 🤖 Commands

- `/start` — Displays a welcome message (custom for a specific user).
- `/help` — Sends a sarcastic help message.
- `/lowercase` or `/lower` — Sets mode to lowercase.
- `/uppercase` or `/upper` — Sets mode to uppercase.
- `/capitalise` — Sets mode to capitalised text.
- `/capitalize` — Joke response (no offense to American spelling).
- `/langXX` — Responds with a humorous language setting message (does nothing).

---

## 🧠 How it works

- When you send a command, your mode is updated in the SQLite database.
- Normal text messages are transformed according to your selected mode.
- The bot uses asynchronous SQLite access and Aiogram’s dispatcher for efficient updates.
- All configuration is handled via `thecasebot.conf` — no more hardcoding secrets!

---

## ⚠️ License & Rights

© Alssandrx 2025. All rights reserved unless specified otherwise upon request.

---

> _“If you’re reading this, you’re probably bored. Go outside or write your own bot!”_
