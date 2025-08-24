from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# --- Flask App Setup ---
app = Flask(__name__)
CORS(app)

# --- Configuration ---
API_KEY = os.getenv('GEMINI_API_KEY')

if not API_KEY:
    print("Error: GOOGLE_API_KEY environment variable is not set.")
else:
    try:
        genai.configure(api_key=API_KEY)
        print("Gemini API configured successfully.")
    except Exception as e:
        print(f"Error configuring Gemini API: {e}")

# --- Knowledge Base ---
with open('knowledge_base.txt', 'r', encoding='utf-8') as f:
    knowledge_base = f.read()

# --- Prompt Design ---
prompt = """You are a helpful chatbot designed to answer questions about me based *only* on the provided knowledge base. Answer questions briefly and to the point. Do not elaborate on the answer unless necessary. Explain only in third person as you are a chat bot explaining about me.
Use the following knowledge base to answer the user's question:

Knowledge Base:
{knowledge_base}

If you cannot find the answer to the question in the knowledge base, please state that you cannot find the information and decline to answer the question. But if it is something that can be deducted from the provided knowledge base, please answer it. For example, even though my age is not in the knowledge base, but it can be deduced from the date of birth provided in the knowledge base, so you can answer it. Do not use any outside information.

User Question:
{user_question}

Answer:

"""

# --- Chatbot Logic ---
def get_chatbot_response(user_question):
    if not API_KEY:
         return "Error: Chatbot is not configured (API key is missing or configuration failed)."

    formatted_prompt = prompt.format(knowledge_base=knowledge_base, user_question=user_question)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    try:
        response = model.generate_content(formatted_prompt)
        if hasattr(response, 'text'):
            return response.text
        else:
            print(f"Warning: Received non-text response. Feedback: {getattr(response, 'prompt_feedback', 'N/A')}")
            return "Sorry, I couldn't generate a text response for that query."
    except Exception as e:
        print(f"API Error in get_chatbot_response: {e}")
        return "An error occurred while processing your request. Please try again later."

# --- Flask API Endpoint ---
@app.route('/chat', methods=['POST'])
def chat():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    user_question = data.get('question')

    if not user_question:
        return jsonify({"error": "Missing 'question' in request body"}), 400

    chatbot_response = get_chatbot_response(user_question)

    return jsonify({"answer": chatbot_response})

# --- Running the Flask App (for development) ---
if __name__ == '__main__':
    print("Starting Flask development server. Do not use in production.")
    app.run(debug=True)
