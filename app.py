import streamlit as st
from utils import (
    get_api_key,
    generate_excuse,
    format_chat_proof,
    text_to_speech,
    show_emergency_alert,
)

def main():
    st.set_page_config(page_title="AI Excuse Generator")
    st.title("🤖 AI Excuse Generator")

    api_key = get_api_key()
    if not api_key:
        st.error("Set GEMINI_API_KEY as an environment variable.")
        st.stop()

    scenario = st.text_area("Describe your situation:")

    if st.button("Generate"):
        if not scenario.strip():
            st.warning("Please enter a scenario.")
            return

        with st.spinner("Generating..."):
            excuse = generate_excuse(scenario, api_key)

        st.subheader("Excuse")
        st.success(excuse)

        st.subheader("Fake Proof")
        st.code(format_chat_proof(excuse))

        audio_path = text_to_speech(excuse)
        st.audio(audio_path)

        show_emergency_alert()

if __name__ == "__main__":
    main()
