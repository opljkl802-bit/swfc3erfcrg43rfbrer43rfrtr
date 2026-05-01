import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "30296254"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "c2b5306f4ccd2d795405a026c10b4c62")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8543000414:AAG4h4r0HtAZUBH6tnTR0ACM5DjzT33b0hU")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Masterextratorraonebot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7660916897"))
# ------------------X------------------------------
CREATOR_ID = int(os.environ.get("CREATOR_ID", "7660916897"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1001235155926"))


SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7660916897").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001235155926"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://yakujaae_db_user:pubg1290@cluster0.jvawywm.mongodb.net/?appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1001235155926"))
