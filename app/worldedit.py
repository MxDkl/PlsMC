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
        I will provide documentation for some commands you may need to use.
        Manditory command arguments are surrounded by <>, and optional arguments are surrounded by [].
        Assume the user does not want a brush unless specified.
        Some commands may require a region to be selected.
        Some keywords and their meanings:
        shape: the shape of the region; can be cuboid, cyl, sphere
        radius: the radius of the region; a number
        density: the density of the region; a number lower=more dense
        type: changes depending the command; can be block; biome; tree
        pattern: the pattern of the region; can be block, biome, tree
        Here is the documentation:
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