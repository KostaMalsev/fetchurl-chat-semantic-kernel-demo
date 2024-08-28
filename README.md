This repository contains a demo project for integrating URL fetching capabilities into a chat application using Semantic Kernel. 
The aim of this repo is to showcase how semantic analysis and natural 
language processing can be leveraged to enhance chat interactions by dynamically fetching and processing content from web URLs.

README for fetchurl-chat-semantic-kernel-demo
Overview
This repository contains a demo project for integrating URL fetching capabilities into a chat application using Semantic Kernel. The aim of this repo is to showcase how semantic analysis and natural language processing can be leveraged to enhance chat interactions by dynamically fetching and processing content from web URLs.

Repository Contents
static/ - Contains static files.
.env - Environment variable configurations.
.env.example - Example environment configuration file.
.gitignore - Git ignore file.
Dockerfile - Docker configuration.
README.md - This file.
api-key.txt - Placeholder for API key storage.
app.py - Main application script.
docker-compose.yml - Docker Compose configuration.
fetchurl.py - Script for fetching URLs.
requirements.txt - Python dependencies.
simple-test.py - Simple test script for validating functionality.
Instructions to Run the Demo
Clone the Repository

git clone https://github.com/KostaMalsev/fetchurl-chat-semantic-kernel-demo
cd fetchurl-chat-semantic-kernel-demo
Setup Environment Variables

Copy the example .env file and adjust with your configurations.
cp .env.example .env
Install Dependencies

It's recommended to use a virtual environment.
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run the Application

You can run the application using Docker or directly with Python.
Using Docker:

docker-compose up
Using Python directly:

python app.py
Test the URL Fetching Functionality

python simple-test.py
Additional Information
Homepage: fetchurl-chat-semantic-kernel-demo.vercel.app