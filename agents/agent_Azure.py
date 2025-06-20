#pip install 'smolagents[openai]'
# https://huggingface.co/docs/smolagents/guided_tour?Pick+a+LLM=Azure+OpenAI
from smolagents import CodeAgent, AzureOpenAIServerModel
from tool import save_script_to_tests_folder, save_screenshot_to_tests_folder
from dotenv import load_dotenv
import os
load_dotenv()
azure_endpoint = os.getenv("AZURE_ENDPOINT")
azure_api_key = os.getenv("AZURE_API_KEY")

model = AzureOpenAIServerModel(model_id="gpt-4.1-mini-Yeo",
                               api_version="2024-12-01-preview",
                               azure_endpoint=azure_endpoint,
                               api_key=azure_api_key)
agent = CodeAgent(
    tools=[save_script_to_tests_folder, save_screenshot_to_tests_folder],
    model=model,
    additional_authorized_imports=[
        "playwright",
        "playwright.sync_api",
        "playwright.async_api",
        "os",
        "agents.tool",
        "time",
        "re"
    ]
)

def load_prompt(prompt_filename: str) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(base_dir, '..', 'prompts', prompt_filename)

    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

# 👉 Choose your prompt
prompt = load_prompt("Playright_homepage_searchAzure.txt")

# 👇 Run agent with the prompt
generated_code = agent.run(prompt, max_steps=3)

print("Script generation with Azure is completed!")