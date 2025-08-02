from azure.ai.ml.entities import Workspace
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

subscription_id = os.getenv("SUBSCRIPTION_ID")
resource_group = os.getenv("RESOURCE_GROUP")

if not subscription_id or not resource_group:
    raise ValueError(
        "Please set the SUBSCRIPTION_ID and RESOURCE_GROUP in your .env file."
    )

# Configure the ML client
ml_client = MLClient(
    credential=DefaultAzureCredential(),
    subscription_id=subscription_id,
    resource_group_name=resource_group,
)

# Configure the workspace
workspace_name = "mlw-example"
ws_basic = Workspace(
    name=workspace_name,
    location="swedencentral",
    resource_group=resource_group,
    display_name="ML Workspace Example",
    description="This is a basic example of an Azure ML workspace.",
)

# Create the workspace
poller = ml_client.workspaces.begin_create(ws_basic)
workspace = poller.result()

print(f"Workspace '{workspace.name}' is now in state '{workspace.status}'.")
