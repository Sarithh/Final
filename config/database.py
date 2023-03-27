from pymongo import MongoClient
import ssl
from core import config

ssl._create_default_https_context = ssl._create_unverified_context

client = MongoClient(f'mongodb+srv://{config.settings.username}:{config.settings.password}@{config.settings.host}/test')

db = client.concey

collection_name = db["express"]
