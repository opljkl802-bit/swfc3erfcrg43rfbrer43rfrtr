import os
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client
from cleanup import start_cleanup_scheduler

# Start the cleanup scheduler
scheduler = start_cleanup_scheduler()

# Flask app setup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Tech VJ'

def run_flask():
    # Render automatically sets PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# Start Flask in a separate thread
Thread(target=run_flask, daemon=True).start()

# --- Fetch credentials from environment variables ---
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("SESSION_STRING") # Yeh line add kardi hai

# --- Pyrogram bot setup ---
bot = Client(
    "my_bot",
    api_id=int(API_ID) if API_ID else None, # String ko integer mein convert kiya
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    sleep_threshold=60,  # Wait 60 seconds before reconnecting
    max_retries=5  # Retry 5 times before giving up
)

@bot.on_message()
async def my_handler(client, message):
    await message.reply("Hello from Tech VJ Bot!")

async def main():
    try:
        await bot.start()
        print("Successfully started the bot!")
        # Bot ko chalu rakhne ke liye idle loop
        from pyrogram import idle
        await idle()
    except Exception as e:
        print(f"Error starting bot: {e}")
    finally:
        if bot.is_connected:
            await bot.stop()

if __name__ == "__main__":
    # Flask ke liye asyncio loop handle karna
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
