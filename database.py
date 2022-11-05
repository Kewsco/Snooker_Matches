from sqlite3 import Cursor
import pyodbc as odbc
from player import Player

# A class to connect to the database and perform data retirieval. 
class Database:
    def __init__(self):
        self.db = None        
    
    def ConnectToDB(self) -> odbc.Connection:
        self.db = odbc.connect("""
            DRIVER=SQL SERVER;
            SERVER=.\SQLEXPRESS;
            DATABASE=SnookerDB;
            Trust_Connection=yes;    
        """)
        return self.db
    
    def GetPlayerByID(self, player_id) -> Player:
        cursor = self.db.cursor()
        query = f"SELECT * FROM [dbo].[Player] WHERE [player_id] = {player_id}"
        pd = cursor.execute(query).fetchone()
        player = Player(id=pd.player_id,
                        firstname=pd.first_name,
                        lastname=pd.last_name,
                        nationality=pd.nationality,
                        dob=pd.dob,
                        gender=pd.gender)
        return player