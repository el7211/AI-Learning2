# AI_Learning2

This project demonstrates the use of AI agents to automate web testing workflows. The architecture includes modular agents powered by different AI models, prompt templates for task definitions, and test scripts generated from agent outputs.

## 📁 Project Structure



### 🔹 `agents/`

Contains 3 AI agents, each powered by a different language model. These agents are responsible for:

- Parsing test requirements from prompts
- Generating Python scripts using frameworks like Selenium or Playwright
- Optionally, validating the test script logic

### 🔹 `prompts/`

This folder stores prompt templates in plain text files. Each prompt defines the web testing steps to perform, such as:

- Visiting a specific page
- Detecting the language of localized content
- Performing UI interactions (e.g., clicking buttons, searching)

### 🔹 `tests/`

Generated test scripts, mostly in Python. These scripts are created based on prompts and model outputs, and can be executed directly with 'python3'

## ✅ Use Cases

- Web UI smoke testing
- Multilingual content verification
- Automating test script creation with LLMs

## 🛠️ Tech Stack

- Python 3.x
- Selenium / Playwright
- Hugging Face / Azure 
- Custom LLM agents

## 🚀 Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/el7211/AI_Learning2.git
   cd AI_Learning2
