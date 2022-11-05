from player import Player
# A class to represent a single match, containing two Players.
class Match:
    def __init__(self, pOne:Player, pTwo:Player, event:int, date:str):
        self.p1 = pOne
        self.p2 = pTwo
        self.event = event
        self.date = date
    
    def PrintMatchDetails(self):
        if self.p1.firstname == 'TBD' or self.p2.firstname == 'TBD':
            print(f"{(self.p1.GetFullName() + ' -VS- ' + self.p2.GetFullName()).rjust(40, '.')} - {str(self.event)}")
        else:
            print(f"{(self.p1.GetFullName() + ' -VS- ' + self.p2.GetFullName()).ljust(40, '.')} - {str(self.event)}")