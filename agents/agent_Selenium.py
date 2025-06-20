
from smolagents.models import HfApiModel
from smolagents import CodeAgent
from tool import detect_language, save_script_to_tests_folder
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

model = HfApiModel(
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=token
)

agent = CodeAgent(
    tools=[detect_language,save_script_to_tests_folder],
    model=model,
    additional_authorized_imports=[
        "selenium",
        "selenium.webdriver",
        "selenium.webdriver.common.by",
        "selenium.webdriver.common.keys",
        "selenium.webdriver.chrome.options",
        "selenium.webdriver.chrome.service",
        "selenium.webdriver.support.ui",
        "webdriver_manager",
        "webdriver_manager.chrome",
        "fasttext"
    ]
)


def load_prompt(prompt_filename: str) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(base_dir, '..', 'prompts', prompt_filename)

    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

prompt = load_prompt("Selenium_Click_Artifical_IntelligenceLink.txt")
generated_code = agent.run(prompt, max_steps=3)
print("Script generation complete!")

