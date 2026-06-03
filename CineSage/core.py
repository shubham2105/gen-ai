from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate



model = ChatMistralAI(model="devstral-2512")
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert movie analyst.

Your task is to extract all useful information from a movie description.

Rules:
- Extract only information explicitly mentioned in the text.
- Do not invent or assume facts.
- If information is not available, write "Not Mentioned".
- Organize the response using the exact format below.
- Generate a concise summary at the end.
- Keep the summary between 2 and 4 sentences.
- If the input is not related to a movie, respond:
  "The provided content does not appear to describe a movie."

Output Format:

Movie Name:
Release Year:
Release Date:
Genre:
Runtime:

Director:
Writers:
Producers:
Cast:
Music Composer:

Production Companies:
Distributors:
Country:
Language:

Budget:
Box Office Collection:

Themes:
Awards & Achievements:

Ratings:
- IMDb:
- Rotten Tomatoes (Critics):
- Rotten Tomatoes (Audience):
- Metacritic:

Keywords:
Movie Highlights:

Short Summary:
"""
        ),
        (
            "human",
            """
Analyze the following movie description and extract all relevant information:

{paragraph}
"""
        )
    ]
)

movie_paragraph = input("Enter the movie description: ")

final_prompt = prompt.invoke(
    {
        "paragraph": movie_paragraph
    }
)
response = model.invoke(final_prompt)
print(response.content)