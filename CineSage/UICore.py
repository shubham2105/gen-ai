
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


# Page Config
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Paste a movie description below and extract structured movie information.")


# LLM
model = ChatMistralAI(model="devstral-2512")


# Prompt
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
- Do not use Markdown formatting.
- Do not use bold, italics, headings, bullet points, or code blocks.
- Return plain text only.
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


# Input Area
movie_paragraph = st.text_area(
    "Movie Description",
    height=300,
    placeholder="Paste the movie description here..."
)


# Analyze Button
if st.button("Extract Information", use_container_width=True):

    if not movie_paragraph.strip():
        st.warning("Please enter a movie description.")
    else:
        with st.spinner("Analyzing movie description..."):

            final_prompt = prompt.invoke(
                {
                    "paragraph": movie_paragraph
                }
            )

            response = model.invoke(final_prompt)

        st.subheader("Extracted Information")
        st.markdown(response.content)

