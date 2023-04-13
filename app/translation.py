import wrapper


class Translation(wrapper.openaiWrapper):
    def __init__(self, message : str, languages : tuple):
        super().__init__()
        self.message = message
        self.user_message = "Translate this message to "+languages[0]+" from "+languages[1]+". Reply with only your answer. Do not explain your reasoning or preface your response in any way: " + message

    def getTranslation(self):
        self.translation = self.complete(self.user_message)
        return self.translation