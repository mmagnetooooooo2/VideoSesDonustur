import os
from os import environ
from dotenv import load_dotenv
from pyrogram import Client
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

LOGGER = logging

if os.path.exists('config.env'):
    load_dotenv('config.env')

quee = []

APP_ID = int(environ.get("APP_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
STRING_SESSION = environ.get("STRING_SESSION") 
PRE_LOG = environ.get("PRE_LOG")
DOWNLOAD_DIR = environ.get("DOWNLOAD_DIR", "downloads")
ENCODE_DIR = environ.get("ENCODE_DIR", "encodes")
SUDO_USERS = list(set(int(x) for x in environ.get("SUDO_USERS").split()))

userbot = Client(
    'userbot',
    session_string=STRING_SESSION,
    api_id=APP_ID,
    api_hash=API_HASH,
)
userbot.start()
