# LangChain-Practile: Research Paper Summarization Tool

## Overview
**LangChain-Practile** is a learning project where I explored the LangChain library to build a research paper summarization tool. This tool uses the open-source language model **TinyLlama/TinyLlama-1.1B-Chat-v1.0** (via Hugging Face API) to summarize research papers. For the demo, I summarized the famous *"Attention Is All You Need"* paper, which introduced the Transformer architecture. The frontend is built using **Streamlit** to provide a simple user interface for interacting with the tool.

This project was created for practicing and learning:
- Prompt engineering with LangChain.
- API integration with Hugging Face.
- Building a practical AI tool for research purposes.
- Creating a basic frontend with Streamlit.

## Features
- Summarizes research papers using LangChain's prompt templates.
- Powered by the lightweight **TinyLlama-1.1B-Chat-v1.0** model.
- API integration with Hugging Face for model inference.
- A Streamlit-based frontend for user interaction.
- Easy-to-use script for generating summaries.

## Folder Structure
- **prompt_generator.py**: Core script that handles the summarization logic using LangChain and TinyLlama.
- **prompt_ui.py**: Script for experimenting with Hugging Face API and prompt templates.
- **prompt_template.json**: JSON file containing the prompt templates used for summarization.
- **requirements.txt**: List of dependencies required to run the project.
- **.gitignore**: Standard Git ignore file to exclude unnecessary files.

## Prerequisites
- Python 3.8 or higher.
- A Hugging Face API token to access the TinyLlama model.
- A basic understanding of LangChain and Streamlit.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/MukeshJangid17/LangChain-practile.git
   cd LangChain-practile

2. Install the required dependencies
   ```bash
   pip install -r requirements.txt
3. Set up your Hugging Face API token as an environment variable:
   ```bash
   export HF_API_TOKEN="your-huggingface-api-token"

## Usage
1. Run the Streamlit app to launch the frontend in the cmd:
   ```bash
   streamlit run prompt_ui.py
2. Open the provided local URL (usually http://localhost:8501) in your browser.
3. Use the Streamlit interface to input a research paper or text, and the tool will generate a summary using the TinyLlama model.
4. To experiment with prompt templates, modify the prompt_template.json file.

## Learning Goals
This project was built for practice and learning purposes, focusing on:

* Understanding how to use LangChain for prompt engineering.
* Working with open-source LLMs like TinyLlama via Hugging Face API.
* Building a simple frontend with Streamlit.
* Creating a practical tool for research paper summarization.

## Future Improvements
* Add support for more advanced LLMs for better summarization.
* Enhance the Streamlit frontend with more features (e.g., file upload for PDFs).
* Improve prompt templates for more accurate and detailed summaries.
* Add error handling for API requests.

## Contributing
This is a learning project, but contributions are welcome! Feel free to fork the repository, experiment, and share your ideas. If you have suggestions, open an issue or submit a pull request.
  
