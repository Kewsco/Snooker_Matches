import requests
import json
from database import Database

#Python3 - This script gets every single player provided by the API and stores them into a local database. 

def InsertAllPlayersIntoDB() -> None:
    playerURL:str = "http://api.snooker.org/?p="
    playerid = 1
    playerErrorCount = 0
    db = Database().ConnectToDB()
    while True:
        playerReq = requests.get(playerURL + str(playerid))
        playerJSON = json.loads(playerReq.text)
        if not playerJSON[0]:
            print("Player Error")
            playerErrorCount += 1
            playerid += 1
        else:
            p = playerJSON[0]
            if "'" in p['FirstName']:
                p = {**p, 'FirstName': NameFormatter(p['FirstName'])}
            
            if "'" in p['LastName']:
                p = {**p, 'LastName': NameFormatter(p['LastName'])}
            
            query = f"""
                INSERT INTO [dbo].[Player] ([player_id], [first_name], [last_name], [nationality], [dob], [gender])
                VALUES ({playerid}, '{p['FirstName']}', '{p['LastName']}', '{p['Nationality']}', '{p['Born']}', '{p['Sex']}')
                """
            db.cursor().execute(query)
            db.cursor().commit()
            playerid += 1
            playerErrorCount = 0
        if playerErrorCount > 25:
            break

# Format names containing apostrophes. (O'Sullivan, etc.) 
def NameFormatter(name:str) -> str:
    nameChars = list(name)
    for i in range(len(nameChars)):
        if nameChars[i] == "'":
            nameChars[i] = "\'\'"
    formattedName = ""
    return formattedName.join(nameChars)

if __name__ == "__main__":
    InsertAllPlayersIntoDB()