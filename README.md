# ai-chatbot-python
🚀 A collection of simple and practical AI chatbot examples built in Python. This repository demonstrates how to integrate with Generative AI APIs (Gemini, OpenAI, Hugging Face, etc.) and create conversational chatbots for terminal or application use.

# Chat with Gemini (Python)

This is a simple Python script to interact with **Google's Gemini API** using the official `google-generativeai` package.  
It creates a chat session where the model remembers context across turns.

---

## 🚀 Setup

1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/chat-with-gemini.git
   cd chat-with-gemini

2. **Install dependencies**
   ```bash
   pip install google-generativeai

3. **Get a Gemini API key**
   Go to Google AI Studio
   Sign in with your Google account.
   Click Create API key.
   Copy the key.

4. **Set your API key (do NOT hardcode it in the script!)**
   👉 Option A: Export it as an environment variable:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"

   On Windows (PowerShell):
   ```powershell
   setx GEMINI_API_KEY "your_api_key_here"

   👉 Option B: Create a .env file (recommended for local dev):
   ```ini
   GEMINI_API_KEY=your_api_key_here

5. **Run the script**
   ```bash
   python chat_with_gemini.py

6. **💬 Example Usage**
   ```text
   You: Hello Gemini!
   Gemini: Hi there! How can I help you today?

   You: Tell me a fun fact.
   Gemini: Did you know octopuses have three hearts?

7. **📂 Repository Structure**
   ai-chatbot-python/
   ├── chat_with_gemini.py   # Main chatbot script
   ├── requirements.txt      # Python dependencies
   ├── .gitignore            # Ignore sensitive & unnecessary files
   ├── LICENSE               # Open-source license
   └── README.md             # Project documentation

8. **Install dependencies**
   Once the file is in your repo, users can just run:
   ```bash
    pip install -r requirements.txt

9. **📜 License**
   This project is licensed under the MIT License.
