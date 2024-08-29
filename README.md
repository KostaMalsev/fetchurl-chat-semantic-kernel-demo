This demo project for integrating URL fetching capabilities into a chat application using Semantic Kernel. 

Overview
In this demo, we will use Semantic Kernel to integrate a custom plugin written in python. 
This plugin is designed to extract web content from URLs specified within the chat prompt.

Repository Contents
static/ - Contains static files.
.env - Environment variable configurations.
.env.example - Example environment configuration file.
.gitignore - Git ignore file.
Dockerfile - Docker configuration.
api-key.txt - Placeholder for API key storage.
app.py - Main application script.
docker-compose.yml - Docker Compose configuration.
fetchurl.py - Script for fetching URLs.
requirements.txt - Python dependencies.

Instructions to Run the Demo
Clone the Repository:
git clone https://github.com/KostaMalsev/fetchurl-chat-semantic-kernel-demo
cd fetchurl-chat-semantic-kernel-demo

You can run the application using Docker or directly with Python.
Using Docker:
docker-compose up

Test demo from browser at http://localhost:8000/static/webclient.html

Using Python directly:
python app.py

