from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
model_mistral = ChatMistralAI(model="devstral-2512")

# implementing prompt template for different modes of chatbot
print("Choose yout AI mode")
print("1 for Angry mode")
print("2 for Funny mode")
print("3 for Sad mode")

choice = int(input("Enter your choice : "))
if choice == 1:
    mode = "You are an angry Ai Agent, respond aggresively to the user and be impatient"
elif choice == 2:
    mode = "You are a funny Ai Agent, respond in a humorous way to the user and be playful"
elif choice == 3:
    mode = "You are a sad Ai Agent, respond in a melancholic way to the user and be empathetic"

messages = [
    SystemMessage (content = mode)
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