from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()

# using model class to envoke huggingface model
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    temperature=0.7,
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("Who is Lionel Messi?")
print(response.content)