from database import Database
from NoMatchException import NoMatchException
from match import Match
import datetime, requests, json, pprint

def GetTodaysMatches()->list:
    todaysMatches = []
    matches = requests.get("http://api.snooker.org/?t=14")
    jsonData = json.loads(matches.text)
    match = 0
    formattedDay = f"{dt.year}-{dt.month:02d}-{dt.day:02d}"
    while True:
        if(formattedDay in jsonData[match]['ScheduledDate']):
            todaysMatches.append(jsonData[match])
            match += 1
        else:
            break
    return todaysMatches

if __name__ == '__main__':
    dbObj = Database()
    dbObj.ConnectToDB()
    matches:list[Match] = []
    dt = datetime.datetime.now()
    print(f"Getting Games For {dt.day:02d}-{dt.month:02d}-{dt.year} \n")
    todaysMatches = GetTodaysMatches()
    if not todaysMatches:
        print("There are no snooker matches being played today.")
    else:
        for match in todaysMatches:
            newMatch = Match(dbObj.GetPlayerByID(match['Player1ID']), 
                                dbObj.GetPlayerByID(match['Player2ID']),
                                match['EventID'],
                                match['ScheduledDate'])
            newMatch.PrintMatchDetails()
    input("\nPress Enter to exit")