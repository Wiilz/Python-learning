class GameObject:
    def __init__(self, name):
        self.name = name

    def pickUp(self, player):
        print "player:",player

class Coin(GameObject):
    def __init__(self, value):
        GameObject.__init__(self,"coin")
        self.value = value
    def spend(self,buyer,seller):
        print "buyer:",buyer," seller:",seller

myCoin = Coin(20)
print myCoin.name
print myCoin.value
myCoin.pickUp("user")
myCoin.spend("buyer","seller")

