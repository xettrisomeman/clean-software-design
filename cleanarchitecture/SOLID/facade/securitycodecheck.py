

class SecurityCodeCheck:

    def __init__(self):
        self.__securityCode = 1234


    def getSecurityCode(self):
        return self.__securityCode

    
    def isCodeCorrect(self, secCodeToCheck):
        if secCodeToCheck == self.getSecurityCode():
            return True
        else:
            return False

