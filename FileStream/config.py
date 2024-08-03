import os
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", 25833520))
    API_HASH = str(env.get("API_HASH", "7d012a6cbfabc2d0436d7a09d8362af7"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "5585418491:AAEFnQ6TiBTq5liqw9_JBjHSANs-4xkSMB8"))
    OWNER_ID = int(env.get('OWNER_ID', '1562935405'))
    try:
        ADMINS=[]
        for x in (os.environ.get("ADMINS", "563896360 974706111 1562935405 921365334").split()):
            ADMINS.append(int(x))
    except ValueError:
            raise Exception("Your Admins list does not contain valid integers.")
    
    WORKERS = int(env.get("WORKERS", "1000"))  # 100 workers = 100 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', 'mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', None))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', '-1002224312828')
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', True)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://telegra.ph/file/54c270aac33943345b479.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", -1001611644647))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", -1001611644647))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8000))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "f256645-23f6aa42f946.herokuapp.com")) #"185.133.248.85")) 
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    KEEP_ALIVE = bool(env.get("KEEP_ALIVE", "True"))
    HAS_SSL = str(env.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )
