# https://github.com/dataprofessor/multi-page-app/blob/main/multiapp.py
import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, func):
        self.apps.append(func)