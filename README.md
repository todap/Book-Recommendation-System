# 📚 Book Recommendation System
Welcome to the Book Recommendation System! This application helps you find popular books in your favorite genres and recommends the best book based on your reading preferences.

### Features
Search Popular Books by Genre: Get a list of 100 popular books in any genre.
Filter Top 10 Books: Narrow down the list to the top 10 most popular books.
Personalized Recommendation: Select the best book based on your specific reading preferences.
### Installation
## Prerequisites
Python 3.8 or higher
Streamlit
Requests
Dotenv
Langchain
### Clone the Repository
```bash
git clone https://github.com/yourusername/book-recommendation-system.git
cd book-recommendation-system
```
### Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate
```
### Install Dependencies
```pip
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a .env file in the root directory and add your Huggingface API token:
```plaintext
HUGGINGFACE_TOKEN=your_huggingface_api_token
```
### Usage
Run the Streamlit application:
```bash
streamlit run app.py
```

### Using the Application
- Enter a Genre: Start by typing a genre in the input box and press Enter.
- View Top 10 Books: The application will fetch and display the top 10 books in the specified genre.
- Enter Your Preferences: Provide your reading preferences (e.g., "adventure, strong female lead") and get a personalized book recommendation.
