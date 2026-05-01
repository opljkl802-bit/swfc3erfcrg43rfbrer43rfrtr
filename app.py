import os
from flask import Flask
from threading import Thread
from pyrogram import Client
import asyncio
from cleanup import start_cleanup_scheduler

# Start the cleanup scheduler
scheduler = start_cleanup_scheduler()

# Your existing app code continues here...

# Flask app to keep Heroku dyno alive
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Tech VJ'

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Start Flask in a separate thread
Thread(target=run_flask).start()

# Fetch credentials from environment variables
import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Pyrogram bot setup with reconnection logic
# Example initialization
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=SESSION_STRING # Isse session file ki zaroorat nahi padegi
)
@bot.on_message()
async def my_handler(client, message):
    await message.reply("Hello from Tech VJ Bot!")

async def main():
    try:
        await bot.start()
        print("Bot Started!")
        # Baaki ka logic yahan...
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if bot.is_connected:
            await bot.stop()

if __name__ == "__main__":
    bot.run(main())
