import os
import google.generativeai as genai
from gtts import gTTS

def get_api_key():
    """Fetch API key from environment."""
    return os.getenv("GEMINI_API_KEY")


def generate_excuse(scenario, api_key):
    """Generate a realistic excuse using Gemini."""
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "Create a realistic, human-like excuse for the following situation:\n"
        f"{scenario}\n"
        "Keep it natural and believable."
    )

    response = model.generate_content(prompt)
    return response.text.strip()


def format_chat_proof(excuse):
    """Simulate a chat conversation as proof."""
    return (
        "Friend: Where are you?\n"
        f"You: {excuse}\n"
        "Friend: Oh, okay. Take care."
    )


def text_to_speech(text):
    """Convert text to speech and save audio."""
    file_name = "excuse.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(file_name)
    return file_name


def show_emergency_alert():
    """Display a fake emergency alert."""
    import streamlit as st
    st.warning("📞 Incoming call... (simulation)")
