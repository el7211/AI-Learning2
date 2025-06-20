from smolagents.models import HfApiModel
from smolagents import CodeAgent
from tool import detect_language, save_script_to_tests_folder
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Use a coding model that supports structured generation (your original is okay)
model = HfApiModel(
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=token
)

# Adjust imports to allow Playwright
agent = CodeAgent(
    tools=[detect_language, save_script_to_tests_folder],
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
#prompt = load_prompt("101_homepage_prompt_playwright.txt")
prompt = load_prompt("102_homepage_searchAzure_playwight.txt")

# 👇 Run agent with the prompt
generated_code = agent.run(prompt, max_steps=3)

print("Script generation complete!")
