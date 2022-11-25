from pymongo import MongoClient
import os
conn = MongoClient(os.environ["DB_URL"])[os.environ["DB_NAME"]]



