from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

# Hugging Face API token
hf_api_token = os.getenv("HUGGINGFACE_API_TOKEN")

llm =  HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="Text Generation",
    huggingfacehub_api_token=hf_api_token
)

model = ChatHuggingFace(llm=llm)


st.header("Reaserch Tool")

paper_input = st.selectbox("Select a research paper", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select a style", ["begineer friendly", "Technical", "Code-Oriented", "Casual"])

length_input = st.select_box("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


