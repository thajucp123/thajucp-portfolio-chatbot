# KnowThaj - Personal Portfolio Chatbot

KnowThaj is an AI-powered portfolio assistant designed to answer questions about Thajudeen CP ("Thaju"). It leverages a custom knowledge base and the advanced capabilities of Google Gemini to provide professional, concise, and human-like responses to visitors.

This backend service is built with Flask and is optimized for seamless integration with a frontend portfolio website.

## 🚀 Features

-   **Context-Aware Responses:** Answers questions using a dedicated `knowledge_base.txt`.
-   **Advanced AI Model:** Powered by the **Google Gemini 2.5 Flash** model.
-   **Secure & Robust:** Implements environment variable management for API keys and CORS for secure cross-origin requests.
-   **Postman Verified:** The backend logic and API responses have been rigorously tested and verified using Postman.
-   **Cloud Ready:** Configured for easy deployment on platforms like Vercel.

## 🛠️ Tech Stack

-   **Language:** Python
-   **Framework:** Flask
-   **AI Engine:** Google Generative AI (Gemini 2.5 Flash)
-   **Environment Management:** python-dotenv
-   **Deployment:** Vercel

## 🔌 API Endpoints

The backend provides the following endpoints for frontend integration:

### 📡 Status Endpoint

**URL:** `/status`  
**Method:** `GET`

**Success Response (200 OK):**
```json
{
  "status": "online",
  "model": "gemini-2.5-flash",
  "assistant": "KnowThaj"
}
```

### 💬 Chat Endpoint

**URL:** `/chat`  
**Method:** `POST`  
**Content-Type:** `application/json`

**Request Body:**
```json
{
  "question": "What are Thaju's top skills?"
}
```

**Success Response (200 OK):**
```json
{
  "answer": "Thaju specializes in Python, Flask, and AI integration. He has extensive experience in building web applications and intelligent chatbots."
}
```

**Error Responses:**
-   `400 Bad Request`: Missing `question` in request body.
-   `415 Unsupported Media Type`: Request is not JSON.
-   `500 Internal Server Error`: API configuration issues or service unavailability.

## 🧪 Development & Testing

The API has been verified using **Postman** to ensure consistent and accurate responses. 

### Local Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/thajucp123/thajucp-portfolio-chatbot.git
    cd thajucp-portfolio-chatbot
    ```

2.  **Environment Configuration:**
    Create a `.env` file in the root directory:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Locally:**
    ```bash
    python app.py
    ```
    The server will start at `http://127.0.0.1:5000`.

## 📦 Deployment

This project includes a `vercel.json` configuration for one-click deployment to Vercel. Ensure you set the `GEMINI_API_KEY` in your Vercel project's environment variables.

---

Built with ❤️ by [Thajudeen CP](https://www.thajucp.in/)
