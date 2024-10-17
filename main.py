import requests
import streamlit as st

# Prepare API key and API url
api_key = "g0g3EQaYRcd4Udfhv3WSPKNDDbpxQ2tYPzQJYStu"
url ="https://api.nasa.gov/planetary/apod"\
      f"api_key={api_key}"

# Get the request data as a dictionary
response_1 = requests.get(url)
data = response_1.json()

# Extract the image title, url and, explanation
title = data["title"]
image_url = data["url"] 
explanation = data["explanation"]

# Download the image
image_filepath = "img.png"
response_2 = requests.get(image_url)
with open(image_filepath,'wb') as file:#Binary mode, which is used for files that are not plain text (like images, audio files, etc.)
    file.write(response_2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
    

