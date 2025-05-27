#!/bin/bash

# Create the .streamlit directory and config file
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml

# Run the Streamlit app
streamlit run app.py
