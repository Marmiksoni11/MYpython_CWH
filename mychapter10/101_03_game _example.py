class Remote():
    def isLeftpressed(self):
     pass 


class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()
if(remote1.isLeftpressed()):
    player1.moveLeft()
elif(remote1.isRightpressed()):
    player1.moveRight()
elif(remote1.isToppressed()):
    player1.moveTop()


player1.printData()
