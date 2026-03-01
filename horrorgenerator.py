import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the environment variable
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=genai.types.GenerationConfig(
        temperature=0.8,
        top_p=0.9,
        top_k=40,
        max_output_tokens=2048
    )
)

# Function to generate horror story
def generate_horror_story(character_name, situation, no_of_lines):
    try:
        prompt = (
            f"Write a horror story of about {no_of_lines} lines. "
            f"The main character is {character_name}. The story should be set in the following situation: {situation}. "
            f"Include eerie plot twists and atmospheric descriptions. Make it spine-chilling."
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while generating the story: {e}"

# Streamlit UI
def main():
    st.set_page_config(page_title="HauntScript: AI Horror Generator", layout="centered")
    st.title("🕯 HauntScript: AI-Driven Horror Story Generator")
    st.write("Enter the details below to generate your custom horror story:")

    character_name = st.text_input("👤 Character Name")
    situation = st.text_input("📍 Situation / Setting")
    no_of_lines = st.number_input("📏 Number of Lines", min_value=1, max_value=100, value=10)

    if st.button("🔮 Generate Story"):
        if not character_name or not situation:
            st.warning("Please provide both a character name and situation.")
            return
        with st.spinner("Generating your horror story..."):
            story = generate_horror_story(character_name, situation, no_of_lines)
            st.subheader("📖 Your Horror Story:")
            st.write(story)

# Run the app
if __name__ == "_main_":
    main()