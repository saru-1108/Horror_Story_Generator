import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load the environment variable
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


# Initialize Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Function to generate horror story
def generate_horror_story(character_name, situation, no_of_lines):
    try:
        prompt = (
            f"Write a horror story of about {no_of_lines} lines. "
            f"The main character is {character_name}. "
            f"The story should be set in the following situation: {situation}. "
            f"Include eerie plot twists and atmospheric descriptions. "
            f"Make it spine-chilling."
        )

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"An error occurred while generating the story: {e}"

# Streamlit UI
def main():
    st.set_page_config(page_title="HauntScript: AI Horror Generator", layout="centered")
    st.title("🕯 HauntScript: AI-Driven Horror Story Generator")
    st.write("Enter the details below to generate your custom horror story:")

    character_name = st.text_input(" Character Name")
    situation = st.text_input(" Situation / Setting")
    no_of_lines = st.number_input(" Number of Lines", min_value=1, max_value=100, value=10)

    if st.button("Generate Story"):
        if not character_name or not situation:
            st.warning("Please provide both a character name and situation.")
            return
        with st.spinner("Generating your horror story..."):
            story = generate_horror_story(character_name, situation, no_of_lines)
            st.subheader("Your Horror Story:")
            st.write(story)

# Run the app
if __name__ == "__main__":
    main()
