import json
import os

import streamlit as st

DEFAULT_CONFIG = {"item": "sugar", "unit": "mL", "quantity": 1.0}


def load_config():
    if os.path.exists("config.json"):
        return json.load(open("config.json"))
    return DEFAULT_CONFIG


def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f)


def init():
    st.set_page_config(
        page_title="xtogram - anything to grams",
        page_icon=None,
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )
