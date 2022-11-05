class NoMatchException(Exception):
    def __init__(self):
        super().__init__("There are no snooker matches being played today.")