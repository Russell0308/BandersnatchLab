from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
from pymongo.server_api import ServerApi


class Database:
    load_dotenv()
    client = MongoClient(getenv("DB_URL"), server_api=ServerApi("1"))

    def seed(self, amount):
        try: 
            self.client.admin.command('ping')
            print('Success!')

        except Exception as e:  
            print(e)
        

    def reset(self):
        pass

    def count(self) -> int:
        pass

    def dataframe(self) -> DataFrame:
        pass

    def html_table(self) -> str:
        pass
