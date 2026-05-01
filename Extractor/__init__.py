import asyncio
import logging
import os
import sys
from pyrogram import Client

# Logging Setup
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# --- Configuration ---
# Hum directly environment variables se values le rahe hain taaki config.py ki dependency khatam ho jaye
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
# Agar aapke paas String Session hai toh ye best hai Render ke liye
SESSION_STRING = os.getenv("SESSION_STRING", None) 

# Validate essential variables
if not API_ID or not API_HASH or not BOT_TOKEN:
    logger.error("API_ID, API_HASH, or BOT_TOKEN missing in Environment Variables!")
    sys.exit(1)

# Initialize Pyrogram Client
# Iska naam 'app' hi rehne dein kyunki baaki modules isse 'from Extractor import app' karke use karte hain
app = Client(
    "NirvanaExtractor",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=SESSION_STRING, # Yeh Render par login issue solve karega
    sleep_threshold=120,
    workers=500
)

# Global variables for bot info
BOT_ID = None
BOT_NAME = None
BOT_USERNAME = None

async def info_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    try:
        # Bot ko start karna taaki info fetch ki ja sake
        await app.start()
        getme = await app.get_me()
        BOT_ID = getme.id
        BOT_USERNAME = getme.username
        BOT_NAME = f"{getme.first_name} {getme.last_name}" if getme.last_name else getme.first_name
        
        # Start karne ke baad stop karna zaroori hai kyunki app.py isse firse start karega
        await app.stop() 
        logger.info(f"Bot Info Loaded: {BOT_NAME} (@{BOT_USERNAME})")
    except Exception as e:
        logger.error(f"Failed to fetch bot info: {e}")

# Initial info fetch run karna
loop = asyncio.get_event_loop()
loop.run_until_complete(info_bot())
