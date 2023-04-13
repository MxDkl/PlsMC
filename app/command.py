import wrapper


class Command(wrapper.openaiWrapper):
    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt
        self.system_message = "You are a helpful assistant. You will generate minecraft commands based on user input. Your response should contain ONLY the command and NEVER any explanation whatsoever, even when you give multiple commands. Start all your commands with a '/'."

    def create(self):
        messages=[
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": self.prompt}
        ]
        return self.chat(messages)