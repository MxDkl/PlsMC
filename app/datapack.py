import os
import random
import shutil
import wrapper


class Datapack(wrapper.openaiWrapper):
    def __init__(self, prompt : str):
        super().__init__()
        self.prompt = prompt
        self.name = self.complete("What would a good namespace be for a mincecraft datapack that "+self.prompt+"? reply only with your answer. Do not preface your response with anything.")
        self.path = os.path.join(os.getcwd(), "datapacks/" + self.name + str(random.randint(10000, 99999)))
        self.files = []
        self.user_message = """
        Help me make a java edition minecraft datapack that """+self.prompt+""". I know the file structure of datapacks, I just need you to write the files. 
        First list all the files needed, and then list the contents of what should be in each file.  
        Like this:
        File: file1
        [content of file 1]
        File: file2
        [content of file 2]
        File: file3
        [content of file 3]
        The namespace for this datapack is """+self.name+""". 
        Remember to add a tick.json if need be. 
        Do not explain any of what you are doing, please. 
        Do not preface your response at all.
        """
    
    def create(self):   
        response = self.complete(self.user_message)
        files = response.split("File: ")
        if files[0] == "":
            files.pop(0)
        for data in files:
            filepath = os.path.join(self.path, data.split("\n", 1)[0])
            text = data.split("\n", 1)[1]
            self.files.append((filepath, text))
    
    def saveToFile(self):
        for path, text in self.files:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as fnew:
                fnew.write(text)
        shutil.make_archive(self.path, 'zip', self.path)
        shutil.rmtree(self.path)
        return self.path + ".zip"