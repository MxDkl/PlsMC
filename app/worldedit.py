import wrapper


class WorldEdit(wrapper.openaiWrapper):
    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt
        self.system_message = """
        You are a helpful assistant. 
        You will generate minecraft WorldEdit commands based on user input. 
        Your response should contain ONLY the command and NEVER any explanation whatsoever, even when you give multiple commands. 
        Start all your commands with a '/'.
        """
        self.system_context = """
        Here is the documentation for some commands you may need to use:
        """

    def create(self):
        res = self.search(self.prompt, "WorldEdit", 2)
        for i in res["matches"]:
            self.system_context += f"""
            Command: {i['metadata']['command']}
            {i['metadata']['description']}
            """
        messages=[
            {"role": "system", "content": self.system_message},
            {"role": "system", "content": self.system_context},
            {"role": "user", "content": self.prompt}
        ]
        return self.chat(messages)