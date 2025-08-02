from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI

try:
    
    # connect to the project
    project_endpoint = "https://generative-ai-project-resource.services.ai.azure.com/api/projects/generative-ai-project"
    project_client = AIProjectClient(            
            credential=DefaultAzureCredential(),
            endpoint=project_endpoint,
        )
    
    # Get a chat client
    chat_client = project_client.inference.get_azure_openai_client(api_version="2025-01-01-preview")
    
    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question: ")
    
    response = chat_client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_prompt}
        ],
    )
    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)