import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="Agentic AI")
        st.header("Welcome to Agentic AI")


        self.page_title = self.config.get_page_title()
        st.set_page_config(page_title=self.page_title)

    def display_header(self):
        st.title(self.page_title)

    def display_options(self):
        llm_options = self.config.get_llm_options()
        usecase_options = self.config.get_usecase_options()
        groq_model_options = self.config.get_groq_model_options()

        selected_llm = st.selectbox("Select LLM:", llm_options)
        selected_usecase = st.selectbox("Select Use Case:", usecase_options)
        selected_groq_model = st.selectbox("Select Groq Model:", groq_model_options)

        st.write(f"Selected LLM: {selected_llm}")
        st.write(f"Selected Use Case: {selected_usecase}")
        st.write(f"Selected Groq Model: {selected_groq_model}")

    def run(self):
        self.display_header()
        self.display_options()
