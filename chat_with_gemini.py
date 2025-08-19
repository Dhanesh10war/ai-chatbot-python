# chat_with_gemini.py

"""
Simple Python script to chat with Google's Gemini API.
"""

import os
import google.generativeai as genai

# Get API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ No API key found. Set GEMINI_API_KEY as an environment variable.")

# Load Gemini model (fast, lightweight version)
genai.configure(api_key=API_KEY)

# Load the model
model = genai.GenerativeModel("gemini-2.0-flash")

# Start a chat session
chat = model.start_chat()

print("💬 Chat with Gemini! Type 'exit' to quit.\n")
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
      print("👋 Ending chat...")
      break

    # Send message and get response
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}\n")
