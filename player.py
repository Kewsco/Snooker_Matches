# Class to represent a Player.
class Player:
    def __init__(self, id:int, firstname:str, lastname:str, nationality:str, dob:str, gender:str):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.nationality = nationality
        self.dob = dob
        self.gender = gender
        
    def PrintPlayer(self):
        print(f"""
            -- Player Information --   
            Name: {self.firstname} {self.lastname} 
            Date of Birth: {self.dob}
            Gender: {self.gender}
            Nationality: {self.nationality}
        """)
            
    def GetFullName(self) -> str:
        return f"{self.firstname} {self.lastname}"
            
        