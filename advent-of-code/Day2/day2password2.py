#Class template for passwords. Allows program to easily evaluate password validity, and to create storable Password objects
class Password:
    def __init__(self, letter, occurrence_spots, pwd):
        self.letter = letter
        self.occurrence_spots = occurrence_spots
        self.pwd = pwd
