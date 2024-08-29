# URL Fetching Chat Application with Semantic Kernel

This demo project integrates URL fetching capabilities into a chat application using Semantic Kernel.

## Overview

In this demo, we use Semantic Kernel to integrate a custom Python plugin. This plugin extracts web content from URLs specified within the chat prompt.

## Repository Contents

- `static/` - Contains webclient HTML
- `.env` - Environment variable configurations
- `.env.example` - Example environment configuration file
- `Dockerfile` - Docker configuration
- `api-key.txt` - Placeholder for API key storage
- `app.py` - Main application script
- `docker-compose.yml` - Docker Compose configuration
- `fetchurl.py` - Script for fetching URLs
- `requirements.txt` - Python dependencies

## Prerequisites

1. Azure account ([step-by-step guide](https://azure.microsoft.com/en-us/free/))
2. GPT4o deployed in Microsoft AI Studio ([step-by-step guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal) steps:#1 to #3)
3. Basic Python knowledge

## Instructions to Run the Demo

### 1. Clone the Repository:

```bash
git clone https://github.com/KostaMalsev/fetchurl-chat-semantic-kernel-demo
cd fetchurl-chat-semantic-kernel-demo
```

### 2. Configuration:

- Update your `AZURE_OPENAI_ENDPOINT` in `docker-compose.yml`
- Update the `api-key.txt` with your `AZURE_OPENAI_API_KEY`

### 3. Run the Application:

You can run the application using Docker or directly with Python.

#### Using Docker:

1. Install Docker Compose ([step-by-step guide](https://docs.docker.com/compose/install/))
2. Run the following command:

```bash
docker-compose up
```

3. Test the demo in your browser at http://localhost:8000/static/webclient.html

**Note:** You can find the Docker image of the service on DockerHub: [chatserver](https://hub.docker.com/r/kostyamalsev/chatserver)

#### Using Python directly:

```bash
python app.py
```

## Key Components

### Semantic Kernel Service (app.py):

- Uses `semantic_kernel` for model invocation with FetchPlugin
- Implements FastAPI endpoint at `localhost:8000/demoprompt` for handling chat prompts
- Uses `fetchurl` for web content retrieval

### Custom FetchPlugin:

```python
class FetchPlugin:
    @kernel_function(name="get_content_from_url", description="Get the content from url")
    def get_content_from_url(self, url: str) -> str:
        return fetch_text_content_from_url(url)
```

### Main Flow:

1. On startup: Sets up kernel with AI service and FetchPlugin
2. On request: Invokes model via kernel with the FetchPlugin
3. Returns model response to web client

## Limitations and Considerations

1. This demo uses a single plugin, but Semantic Kernel supports multiple custom plugins
2. The fetch method is limited and may not work on all websites
3. Be aware of AI API usage costs. Use Azure Cost Management for budgeting and monitoring


## Resources

[Semantic Kernel repo](https://github.com/microsoft/semantic-kernel)

