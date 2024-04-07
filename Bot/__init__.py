import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 28625475)) #API ID
API_HASH = environ.get('API_HASH', 'da4894b36ca60168ba283519ed551606') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '6548973082:AAHc_Ti9hkMPmih7rQawnjBuk_2yFMyqOvE') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://dohaf34622:HpxN7FLUgJek49cs@cluster0.txy5lg8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0') #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 1720819569)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1002033464737))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1002090597173))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', 3)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
