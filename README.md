# 🎙️ AI Voice Assistant

This project is a **voice-enabled AI assistant** built with Python and Streamlit. It lets users **ask questions via speech**, get smart answers from **Meta’s LLaMA-4 Maverick model** via OpenRouter API, and **hear responses spoken aloud** using `pyttsx3`. All interactions are logged to a **Google Sheet** for history tracking.

---

## 🚀 Features

✅ Voice input using your microphone  
✅ AI responses powered by `meta-llama/llama-4-maverick:free` via OpenRouter  
✅ Text-to-speech playback using `pyttsx3`  
✅ Conversation log saved to Google Sheets  
✅ Streamlit-based responsive UI  
✅ Sidebar with model/voice info and chat reset  
✅ Secrets protected using `.env` and `.gitignore`

---

## 🧠 Tech Stack

| Feature        | Tool/Service                       |
|----------------|------------------------------------|
| Voice Input    | `speech_recognition` (Google API) |
| Voice Output   | `pyttsx3` (offline TTS engine)    |
| AI Model       | LLaMA-4 Maverick via OpenRouter   |
| UI             | `streamlit`                       |
| Logging        | Google Sheets API                 |
| Secret Mgmt    | `.env`, `python-dotenv`           |

---

## 📁 Project Structure
```
voice_assistant/
│
├── .env # 🔒 Secrets (API keys)
├── app.py # 🚀 Main Streamlit app
├── config.py # 🔧 Loads environment variables
├── credentials.json # 🔑 Google Sheets credentials (ignored in git)
├── gpt_service.py # 🧠 Handles AI response from OpenRouter
├── logger.py # 📊 Logs interactions to Google Sheets
├── speech_module.py # 🎤 Mic input and speech output
├── requirements.txt # 📦 Python dependencies
└── venv/ # 📁 Virtual environment (ignored)
```

---

## 🔐 Environment Setup

Create a `.env` file with your keys:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
GOOGLE_SHEET_ID=your_google_sheet_id
```

Note: Do NOT commit .env or credentials.json to GitHub. They are ignored in .gitignore.

## 📦 Installation & Running
Clone this repo:
```
git clone https://github.com/DattatrayBodake25/ai-voice-assistant.git
cd ai-voice-assistant
```

Set up virtual environment:
```
python -m venv venv
venv\Scripts\activate   # On Windows
```
Install dependencies:
```
pip install -r requirements.txt
```

Add your .env and credentials.json files.

Run the app:
```
streamlit run app.py
```

## 📝 How It Works (End-to-End)

User speaks → speech converted to text using speech_recognition

Text sent to OpenRouter API → response from LLaMA-4 model

Assistant replies:

- 📄 Printed on screen in chat UI

- 🔊 Read out loud via pyttsx3

Interaction logged → logger.py appends to Google Sheet with timestamp

## 🖼️ UI Preview
<img src="https://via.placeholder.com/700x400.png?text=Streamlit+UI+Placeholder" alt="UI Screenshot" />


## ☁️ Deployment Options
Run locally with Streamlit

Package as .exe with pyinstaller

Deploy to a server using Streamlit Sharing or Render

⚠️ Security & Git Tips
✅ .env and credentials.json are excluded via .gitignore
❌ Never push secrets or service account files to GitHub
✅ Use environment variables and python-dotenv to load them safely


💡 Future Ideas
🔄 Continuous listening mode

🧠 Support for multiple AI models

🌐 Multilingual voice output

🎛️ Settings panel for user control

