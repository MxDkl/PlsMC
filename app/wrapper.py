import os
from dotenv import load_dotenv
import openai
import pinecone

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
pinecone.init(
    api_key = os.getenv('PINECONE_API_KEY'),
    environment = "eu-west4-gcp"
)
index = pinecone.Index("commands")


class openaiWrapper:
    def __init__(self):
        self.message_history = []

        self.chat_model = "gpt-3.5-turbo"
        self.temperature = 0
        self.frequency_penalty = 0
        self.presence_penalty = 0
        self.top_p = 1
        self.max_tokens = 1000

    def getMessages(self):
        return self.message_history

    # one message
    def complete(self, message : str):
        response = openai.ChatCompletion.create(
            model=self.chat_model,
            messages=[{"role": "user", "content": message}],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        response = response["choices"][0]["message"]["content"]
        return response
    
    # chat history
    def chat(self, messages : list):
        response = openai.ChatCompletion.create(
            model=self.chat_model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        response = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": response})
        return response
    
    # moderation
    def moderate(self, message : str):
        response = openai.Moderation.create(
            input=message,
        )
        output = response["results"][0]
        return output
    
    # pinecone search
    def search(self, query : str, namespace : str, top_k : int = 1):
        res = openai.Embedding.create(input=query, engine="text-embedding-ada-002")
        res = index.query(vector=res["data"][0]["embedding"], top_k=2, namespace='WorldEdit', include_metadata=True)
        return res
    
    


