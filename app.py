#importing all libraries 
import streamlit as st
from speech_module import listen_to_microphone, speak_text
from gpt_service import generate_llm_response
from logger import log_to_sheet
import time


#Page Config
st.set_page_config(page_title="🎙️ Voice AI Assistant", layout="centered", initial_sidebar_state="expanded")


# CSS for stylish UI
st.markdown("""
    <style>
    .big-title {
        font-size: 2.8em;
        font-weight: bold;
        color: #1F4E79;
        margin-bottom: 0.3em;
    }
    .small-text {
        font-size: 0.95em;
        color: #6c757d;
        margin-bottom: 1em;
    }
    .chat-bubble {
        border-radius: 12px;
        padding: 12px 18px;
        margin: 8px 0;
        max-width: 90%;
        line-height: 1.6;
        font-size: 1.05em;
        color: black; /* ✅ Text always visible */
    }
    .user-bubble {
        background-color: #cdeffd; /* ✅ Light blue */
        text-align: left;
        border-left: 5px solid #00bcd4;
    }
    .bot-bubble {
        background-color: #def8c7; /* ✅ Light green */
        text-align: left;
        border-left: 5px solid #8bc34a;
    }
    .footer {
        margin-top: 30px;
        font-size: 0.85em;
        color: #999;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.markdown("## Details")
    st.markdown("**Model:** `LLaMA-4 Maverick`")
    st.markdown("**Voice:** System default (pyttsx3)")
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []

    st.markdown("---")
    st.markdown("**💡 Tip:** Speak clearly near your mic for better results.")
    st.markdown("Built with ❤️ by Dattatray Bodake")


# Header
st.markdown('<div class="big-title">🎙️ Voice AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="small-text">Talk to your AI assistant using voice. Responses are short, smart, and spoken back to you!</div>', unsafe_allow_html=True)
st.markdown("---")


# Session State Init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Interaction Button
if st.button("🎤 Start Talking"):
    with st.spinner("🎙️ Listening... Please speak into the mic"):
        user_input = listen_to_microphone()

    if "⚠️" in user_input or user_input.strip() == "":
        st.warning(user_input)
    else:
        with st.spinner("🧠 Thinking..."):
            bot_reply = generate_llm_response(user_input)

        # Saving to history and log BEFORE speaking
        st.session_state.chat_history.append(("🧍 You", user_input))
        st.session_state.chat_history.append(("🤖 Assistant", bot_reply))
        log_to_sheet(user_input, bot_reply)

        # Showing last response immediately before speaking
        for speaker, message in st.session_state.chat_history[-2:]:
            css_class = "user-bubble" if "You" in speaker else "bot-bubble"
            st.markdown(f'<div class="chat-bubble {css_class}"><b>{speaker}:</b><br>{message}</div>', unsafe_allow_html=True)

        # Speaking the response in background thread
        with st.spinner("🔊 Speaking..."):
            speak_text(bot_reply)

        time.sleep(0.3)


#Full Chat History
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### Conversation History")
    for speaker, message in st.session_state.chat_history:
        css_class = "user-bubble" if "You" in speaker else "bot-bubble"
        st.markdown(f'<div class="chat-bubble {css_class}"><b>{speaker}:</b><br>{message}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">📡 Powered by Meta LLaMA| Logging to Google Sheets | Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)