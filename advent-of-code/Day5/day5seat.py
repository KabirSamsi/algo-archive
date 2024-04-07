#Seat class allows storage of 'seats' in array
class Seat:

    def __init__(self, code, row, col):
        self.code = code
        self.row = row
        self.col = col
        self.id = (row*8) + col
