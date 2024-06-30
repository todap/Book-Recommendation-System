# 📚 Book Recommendation System

This Streamlit-based application provides personalized book recommendations based on user-specified genres and preferences. It utilizes the Meta-Llama-3-8B-Instruct model from Hugging Face for natural language processing tasks.

## Features

- Search for popular books by genre
- Filter top 10 books from the search results
- Provide personalized book recommendations based on user preferences

## How it Works

1. **Genre Search**: Enter a genre to fetch 100 popular book titles in that category.
2. **Top 10 Filter**: The system automatically filters the top 10 books from the initial list.
3. **Personalized Recommendation**: Enter your reading preferences to receive a tailored book suggestion from the top 10 list.

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/book-recommendation-system.git
Copy
2. Install the required packages:
pip install -r requirements.txt
Copy
3. Set up your Hugging Face API key in the code:
```python
headers = {"Authorization": "Bearer YOUR_HUGGING_FACE_API_KEY"}
Usage
Run the Streamlit app:
Copystreamlit run app.py
Then follow the on-screen instructions to get book recommendations.
Dependencies

streamlit
requests
langchain

API
This project uses the Hugging Face API to access the Meta-Llama-3-8B-Instruct model. Make sure to replace the API key in the code with your own.

## Environment Variables

This project uses the following environment variables:

- `HUGGINGFACE_TOKEN`: Your Hugging Face API token

To use the application, you need to set this environment variable. You can do this by creating a `.env` file in the project root with the content:
HUGGINGFACE_TOKEN=your_token_here
Copy
Replace `your_token_here` with your actual Hugging Face API token.
