from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
from pymongo.server_api import ServerApi


class Database:

    def __init__(self):
        '''
        Initializes connection to Mongo Atlas
        Sets database and collection variable
        Tests connection to Mongo Atlas remote server
        '''
        load_dotenv()
        self.client = MongoClient(getenv("DB_URL"), tls=True, server_api=ServerApi("1"))
        self.db = self.client['database']
        self.collection = self.db['monster_collection']


    def seed(self, amount):
        '''
        Adds a variable amount of documents(Monsters) to the database collection
        '''
        for i in range(amount):
            document = Monster().to_dict()
            self.collection.insert_one(document)
        
    def reset(self):
        '''
        Empties the "Monsters collection"
        '''
        deleted = self.collection.delete_many({})

        return deleted.deleted_count

    def count(self) -> int:
        '''
        Returns the amount of documents(Monsters) in the "Monsters collection"
        '''
        return self.collection.count()

    def dataframe(self) -> DataFrame:
        '''
        Puts documents(Monsters) into a dataframe
        '''
        documents = self.collection.find()
        df = DataFrame(list(documents))

        return df

    def html_table(self) -> str:
        '''
        Makes the dataframe web ready by changing it to an html table
        '''
        if self.dataframe().empty:
            return None
        else: 
            return self.dataframe().drop('_id', axis=1).to_html()
