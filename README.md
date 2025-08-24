# Thajucp.in Personal Portfolio Chatbot with Google Gemini

This project is a simple, yet powerful, personal chatbot powered by the Google Gemini API. It's designed for [my personal portfolio website](https://www.thajucp.in/), allowing visitors to ask questions about me get intelligent, context-aware answers based on a knowledge base I have provided about myself.

The chatbot is built with Flask, making it a lightweight and easy-to-deploy backend service.

- [Live Demo](https://www.thajucp.in/) (Use the chat bot from the bottom right FAB)

## Features

-   **Personalized Responses:** Answers questions based on a custom knowledge base about myself.
-   **Powered by Gemini:** Leverages the advanced capabilities of Google's Gemini Flash model for natural language understanding.
-   **Flask Backend:** A simple and robust Flask server that exposes a single API endpoint for chat.
-   **Easy to Customize:** Designed for easy customization of the knowledge base and chatbot's personality.
-   **Secure API Key Handling:** Uses environment variables to keep my Google Gemini API key secure.
-   **CORS Enabled:** Cross-Origin Resource Sharing (CORS) is enabled for easy integration with my portfolio website frontend.

## How It Works

The application consists of a single Flask server that listens for POST requests on the `/chat` endpoint. When a request is received with a user's question, the server combines the question with the content of the `knowledge_base.txt` file and a predefined prompt. This combined text is then sent to the Google Gemini API, which generates a response. The response is then sent back to the user.

## Getting Started

Follow these instructions to get the chatbot up and running on a local machine.

### Prerequisites

-   Python
-   `pip` (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    clone the repo or download the files.
    ```bash
    git clone https://github.com/thajucp123/thajucp-portfolio-chatbot.git
    cd thajucp-portfolo-chatbot
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage the project's dependencies.

    *   **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

    *   **On macOS and Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    Install all the required packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    The application uses a `.env` file to manage the Google Gemini API key.

    -   Open the `.env` file and add your Google Gemini API key:
        ```
        GEMINI_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY
        ```
    You can get your API key from the [Google AI Studio](https://aistudio.google.com/).

5.  **Customize the Knowledge Base:**
    Open the `knowledge_base.txt` file and replace the existing content with your own personal and professional information. It currently has descriptions about me. This is the data the chatbot will use to answer questions.

### Running the Application

Once you've completed the setup, you can start the Flask server:

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000`.

### Interacting with the Chatbot

You can interact with the chatbot by sending a `POST` request to the `/chat` endpoint.

**Example using `curl`:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"question": "What is your name?"}' http://127.0.0.1:5000/chat
```

**Example using Postman:**

-   **URL:** `http://127.0.0.1:5000/chat`
-   **Method:** `POST`
-   **Headers:** `Content-Type: application/json`
-   **Body (raw, JSON):**
    ```json
    {
        "question": "Tell me about your projects."
    }
    ```

## Building for Yourself

This project is designed to be a template for your own personal chatbot. Here's how you can customize it further:

-   **`knowledge_base.txt`:** This is the most important file for you to edit. The more detailed and well-structured the information in this file, the better the chatbot's responses will be.
-   **`app.py`:**
    -   **Prompt Engineering:** You can modify the `prompt` variable in `app.py` to change the chatbot's personality, tone, and instructions. The default prompt is designed to be a helpful assistant, but you can make it more formal, casual, or even humorous.
    -   **Model:** The application uses the `gemini-1.5-flash-latest` model by default. You can change this to other models available from the Gemini API if you have different needs.

## File Structure

```
.
├── venv/                   # Virtual environment directory
├── app.py                  # Main Flask application file
├── knowledge_base.txt      # Your personal knowledge base
├── requirements.txt        # Python dependencies
├── .env                    # For storing your API key
└── README.md               # This file
```

## Technology Stack

-   **Backend:** Python, Flask
-   **API:** Google Gemini API
