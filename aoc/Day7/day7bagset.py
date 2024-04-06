#BagSet class stores a bag and its allowed contents

class BagSet:
    def __init__(self, val, contents):
        self.val = val #Bag value
        self.contents = contents #References all bags which are allowed (recursive references to BagSet objects)
