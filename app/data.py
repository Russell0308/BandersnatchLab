from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
from pymongo.server_api import ServerApi


class Database:

    def __init__(self):
        load_dotenv()
        self.client = MongoClient(getenv("DB_URL"), tls=True, server_api=ServerApi("1"))
        self.db = self.client['database']
        try: 
            self.client.admin.command('ping')
            print('Success!')

        except Exception as e:  
            print(e)
        

    def seed(self, amount):
        self.collection = self.db['monster_collection']
        for i in range(amount):
            document = Monster().to_dict()
            self.collection.insert_one(document)
        
    def reset(self):
        pass

    def count(self) -> int:
        pass

    def dataframe(self) -> DataFrame:
        pass

    def html_table(self) -> str:
        pass
