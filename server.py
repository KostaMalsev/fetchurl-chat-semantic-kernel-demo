import os
from typing import Annotated
from dotenv import load_dotenv
import asyncio
from fastapi import FastAPI, Body
from pydantic import BaseModel

from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.open_ai_prompt_execution_settings import (
    OpenAIChatPromptExecutionSettings,
)
from semantic_kernel.functions.kernel_function_decorator import kernel_function
from semantic_kernel.kernel import Kernel

from fetchurl import fetch_text_content_from_url

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class FetchPlugin:
    """Plugin provides fetch of content from url."""

    @kernel_function(name="get_content_from_url", description="Get the content from url")
    def get_content_from_url(self, url: Annotated[str, "The input url"]) -> Annotated[str, "The output is a string"]:
        return fetch_text_content_from_url(url)

async def setup_kernel():
    kernel = Kernel()

    # Check if we're using Azure OpenAI
    if os.getenv('GLOBAL_LLM_SERVICE') != "AzureOpenAI":
        raise ValueError("This script is configured to use Azure OpenAI. Please check your .env file.")

    service_id = "function_calling"
    
    # Azure OpenAI setup
    ai_service = AzureChatCompletion(
        service_id=service_id,
        deployment_name=os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT_NAME'),
        endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
        api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    )
    
    kernel.add_service(ai_service)
    kernel.add_plugin(FetchPlugin(), plugin_name="fetchurl")

    return kernel

kernel = asyncio.run(setup_kernel())

@app.post("/demoprompt")
async def demo_prompt(request: PromptRequest):
    settings: OpenAIChatPromptExecutionSettings = kernel.get_prompt_execution_settings_from_service_id(
        service_id="function_calling"
    )
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto(filters={"included_plugins": ["fetchurl"]})

    result = await kernel.invoke_prompt(
        function_name="prompt_test",
        plugin_name="fetchurl_test",
        prompt=request.prompt,
        settings=settings,
    )
    
    return {"response": str(result)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
