import wrapper


class Moderation(wrapper.openaiWrapper):
    def __init__(self, message : str):
        self.message = message
    
    def getModeration(self):
        self.moderation = self.moderate(self.message)
        return self.moderation

    

    