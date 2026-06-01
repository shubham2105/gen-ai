from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
model_mistral = ChatMistralAI(model="devstral-2512")

# response_mistral = model_mistral.invoke(prompt)
while True:
    print("------------------------ Welcome to the Mistral Chatbot, press 0 to exit ------------------------")
    prompt = input("You : ")
    if prompt == "0":
        break
    response_mistral = model_mistral.invoke(prompt)
    print("Bot : ", response_mistral.content)