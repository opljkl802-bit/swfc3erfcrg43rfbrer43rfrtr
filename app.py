import os
import asyncio
import importlib
from flask import Flask
from threading import Thread
from pyrogram import idle
from Extractor import app as bot  # Aapke __init__.py mein 'app' hai, use 'bot' ki tarah import kiya
from Extractor.modules import ALL_MODULES[cite: 1]

# --- Flask Server for Render Port Binding ---
server = Flask(__name__)

@server.route('/')
def health_check():
    return "Extractor Bot is Running Live!"

def run_flask():
    # Render automatically sets PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    server.run(host='0.0.0.0', port=port)

# Start Flask in a separate thread
Thread(target=run_flask, daemon=True).start()

# --- Main Bot Logic ---
async def start_extractor():
    print(">>> Loading Modules...")
    # Har module ko import karna taaki handlers register ho jayein
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("Extractor.modules." + all_module)
            print(f"Successfully loaded: {all_module}")
        except Exception as e:
            print(f"Error loading module {all_module}: {e}")

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    
    # Bot ko chalu rakhne ke liye idle loop
    await idle()
    
    if bot.is_connected:
        await bot.stop()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

if __name__ == "__main__":
    # Asyncio loop handle karna
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_extractor())
    except KeyboardInterrupt:
        pass
