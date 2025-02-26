class Message():
    def __init__(self,message,status,cssClass):
        self.message = message
        self.status = status
        self.cssClass = cssClass

    def getMessage(self):
        return self.message

    def getStatus(self):
        return self.status
    
    def getCssClass(self):
        return self.cssClass