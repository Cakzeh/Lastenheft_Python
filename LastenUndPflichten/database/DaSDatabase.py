import sqlite3

class db():

    def __init__(self, databaseName:str) -> None:
        self.databaseName = databaseName

        self.database = sqlite3.connect(self.databaseName)
        # self.database.row_factory = sqlite3.Row


    def get_db(self):
        if self.database is None:
            self.database = sqlite3.connect(self.databaseName)
            # self.database.row_factory = sqlite3.Row     
        return self.database 


    def close_db(self):
        if self.database is not None:
            self.database.close()
            self.database = None
