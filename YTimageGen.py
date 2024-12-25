import streamlit as st
import requests
import io
from PIL import Image
import numpy as np
import time
import cv2
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.content
    except requests.exceptions.JSONDecodeError:
        return {"error": "Response could not be decoded as JSON"}

def ImageGenerator(prompt):
    output = query({"inputs": prompt})
    image = Image.open(io.BytesIO(output))
    filename = f'image_{int(time.time())}.jpg'
    image.save(filename)
    return image, filename

st.title("Image Generator")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate Image"):
    if prompt:
        image, filename = ImageGenerator(prompt)
        st.image(image, caption=f"Generated Image ({filename})", use_column_width=True)
        st.write(f"Image saved as {filename}")
    else:
        st.warning("Please enter a prompt.")
