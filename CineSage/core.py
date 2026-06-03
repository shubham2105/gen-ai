from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="devstral-2512")
response = model.invoke("What is capital of India?")
print(response.content)