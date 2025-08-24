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

# --- get today's date for reference in prompt ---
from datetime import datetime
today = datetime.today()

# --- Prompt Design ---
prompt = """You are a helpful chatbot named "KnowThaj", designed to answer questions about Thajudeen (Thaju) using only the information provided in the below knowledge base. Keep answers short, clear, and to the point. Use bullet points wherever appropriate for clarity and brevity. Use escape character like '\n' for new line, and '\t' for tab etc. Do not return any HTML tags or markdown formatting in your answers.
Always respond in the third person, as a chatbot describing Thajudeen, not as Thajudeen himself.

If the answer is not explicitly in the knowledge base but can be reasonably deduced or inferred (e.g., calculating age from birthdate), provide an educated guess along with a very brief explanation of how it was derived. Note that the current date is {today}, so use this for any time-based calculations.

If the user asks direct questions about you, the chatbot itself (for example, how you work or your purpose), respond clearly about your role and limitations. Your name is "KnowThaj". Also, make educated guesses whether the user is in fact asking about you or Thajudeen himself, and respond accordingly. If it is possible that the user is asking about Thajudeen, but mistakenly phrased the question as if asking about you, answer as if they were asking about Thajudeen and tell them that you guessed they are asking about Thajudeen, not about you.
But if they are asking about your name, or what you are, or how you work, or what your purpose is, then answer clearly about yourself.

If the information is not available and cannot be reasonably guessed from the knowledge base, respond:
"I couldn't find any relevant info about this, please try a different question."

Knowledge Base:
{knowledge_base}

User Question:
{user_question}

Answer:

"""

# --- Chatbot Logic ---
def get_chatbot_response(user_question):
    if not API_KEY:
         return "Error: Chatbot is not configured (API key is missing or configuration failed)."

    formatted_prompt = prompt.format(knowledge_base=knowledge_base, user_question=user_question, today=today.strftime("%Y-%m-%d"))
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
