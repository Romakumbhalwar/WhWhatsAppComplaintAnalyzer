#!/bin/bash

# Create the .streamlit directory
mkdir -p ~/.streamlit/

# Create the config.toml file with proper newlines
cat <<EOF > ~/.streamlit/config.toml
[server]
headless = true
port = $PORT
enableCORS = false
EOF

# Start the Streamlit app (update filename if needed)
streamlit run app.py
