from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

# using init chat
model = init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")
response = model.invoke("what is cricket?")
print(response.content)


# using model class
from langchain_google_genai import ChatGoogleGenerativeAI
model_class = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
response_class = model_class.invoke("what is football?")
print(response_class.content)

# using mistral model class
from langchain_mistralai.chat_models import ChatMistralAI
model_mistral = ChatMistralAI(model="devstral-2512")
response_mistral = model_mistral.invoke("what is honeybee?")
print(response_mistral.content)

