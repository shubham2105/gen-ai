from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
model_mistral = ChatMistralAI(model="devstral-2512")

messages = [
    SystemMessage (content = "You are a funny Ai Agent")

]
# response_mistral = model_mistral.invoke(prompt)
while True:
    print("------------------------ Welcome to the Mistral Chatbot, press 0 to exit ------------------------")
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response_mistral = model_mistral.invoke(messages)
    messages.append(AIMessage(content=response_mistral.content))
    print("Bot : ", response_mistral.content)
print(messages)