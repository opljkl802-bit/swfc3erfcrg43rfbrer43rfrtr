import os
import asyncio
import importlib
from flask import Flask
from threading import Thread
from pyrogram import idle
from Extractor import bot  # Ensure 'bot' is initialized in Extractor/__init__.py
from Extractor.modules import ALL_MODULES

# --- Flask Server for Render Port Binding ---
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Extractor Bot is Running Live!"

def run_flask():
    # Render port variable fetch karta hai
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# Flask ko alag thread mein start karein
Thread(target=run_flask, daemon=True).start()

# --- Main Bot Logic (Derived from your __main__.py) ---
async def start_extractor():
    print(">>> Loading Modules...")
    # Saare modules load karna (adda, pw, khan, etc.)
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    try:
        await bot.start()
        print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
        await idle()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if bot.is_connected:
            await bot.stop()
        print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_extractor())
