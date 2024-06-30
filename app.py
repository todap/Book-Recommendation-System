import streamlit as st
import requests
from langchain.tools import BaseTool
import re 
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f"Bearer {os.environ.get('HUGGINGFACE_TOKEN')}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_text(user_prompt):
    try:
        payload = {"inputs": user_prompt}
        result = query(payload)
        if isinstance(result, list) and len(result) > 0 and 'generated_text' in result[0]:
            generated_text = result[0]['generated_text']
            return generated_text
        else:
            st.warning(f"Unexpected response format: {result}")
            return ""
    except Exception as e:
        st.error(f"Error in text generation: {str(e)}")
        return ""

class GenreSearchTool(BaseTool):
    name = "GenreSearch"
    description = "Searches for top 100 books"
    
    def _run(self, tool_input: str) -> list:
        user_prompt = f"""<|begin_of_text|>
<|start_header_id|>system<|end_header_id|>
You are an AI assistant that provides lists of book titles. Respond only with the requested book titles, without any additional text.

<|start_header_id|>user<|end_header_id|>
List 100 popular book titles in the {tool_input} genre. Provide only the titles, separated by commas. Do not include any explanations, numbering, or additional text. The response should contain nothing but the comma-separated list of titles.
<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>"""
        response = generate_text(user_prompt)
        if response:
            pattern = r'<\|start_header_id\|>assistant<\|end_header_id\|>\s*(.*)'
            match = re.search(pattern, response, re.DOTALL)
            if match:
                books_text = match.group(1).strip()
                # Split the text into a list of book titles
                book_list = [book.strip() for book in books_text.split(',')]
                return book_list
        return []

class TopTenFilterTool(BaseTool):
    name = "TopTenFilter"
    description = "Filters the top 10 books from a list of books"
    
    def _run(self, tool_input: str) -> list:
        book_list = eval(tool_input)
        user_prompt = f"""<|begin_of_text|>
<|start_header_id|>system<|end_header_id|>
You are an AI assistant that selects and lists book titles. Respond only with the requested book titles, without any additional text.

<|start_header_id|>user<|end_header_id|>
From this list of books: {', '.join(book_list)}, select the 10 most popular books. Provide only these 10 titles, separated by commas. Do not include any explanations, numbering, or additional text. The response should contain nothing but the comma-separated list of 10 titles.
<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>"""
        response = generate_text(user_prompt)
        
        if response:
            pattern = r'<\|start_header_id\|>assistant<\|end_header_id\|>\s*(.*)'
            match = re.search(pattern, response, re.DOTALL)

            if match:
                books_text = match.group(1).strip()
                # Split the text into a list of book titles
                book_list = [book.strip() for book in books_text.split(',')]
                return book_list

        return []

class UserPreferenceTool(BaseTool):
    name = "UserPreference"
    description = "Selects a book based on user preferences"
    
    def _run(self, tool_input: str) -> str:
        input_dict = eval(tool_input)
        preferences = input_dict['preferences']
        book_list = input_dict['book_list']
        user_prompt = f"""<|begin_of_text|>
<|start_header_id|>system<|end_header_id|>
You are an AI assistant that selects the most suitable book title from a list based on given preferences. Respond only with the chosen book title, nothing else.

<|start_header_id|>user<|end_header_id|>
Book titles:
{book_list}

My reading preferences:
{preferences}

Select the best matching book title.
<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>"""
        response = generate_text(user_prompt)
        if response:
            pattern = r'<\|start_header_id\|>assistant<\|end_header_id\|>\s*(.*)'
            match = re.search(pattern, response, re.DOTALL)
            if match:
                books_text = match.group(1).strip()
                return books_text
        return ""

# Streamlit UI
st.title("📚Book Recommendation System")

genre = st.text_input("Enter a genre:")
if genre:
    with st.spinner("Searching for books..."):
        genre_tool = GenreSearchTool()
        top_books = genre_tool.run(genre)
        st.info(f"Fetched 100 books in the genre: {genre}")
        if top_books:
            top_ten_tool = TopTenFilterTool()
            top_10_books = top_ten_tool.run(str(top_books))
            if top_10_books:
                st.write("\nTop 10 Books:")
                for book in top_10_books:
                    st.write(f"- {book}")
                preferences = st.text_input("Enter your preferences (e.g., 'adventure, strong female lead'):")
                if preferences:
                    with st.spinner("Selecting best book based on preferences..."):
                        user_preference_tool = UserPreferenceTool()
                        user_input = str({"preferences": preferences, "book_list": top_10_books})
                        best_book = user_preference_tool.run(user_input)
                        if best_book:
                            st.success(f"\nRecommended Book: {best_book}")
                        else:
                            st.warning("Unable to select a book based on the given preferences. Please try again with different preferences.")
            else:
                st.warning("Unable to filter top books. Please try a different genre.")
        else:
            st.warning("No books found for the given genre. Please try a different genre.")