# tool.py

import os
from smolagents import tool
import langid
from pathlib import Path

@tool
def detect_language(text: str) -> str:
    """
    Detects the language of the given text using the langid library.

    Args:
        text (str): The input text whose language is to be detected.

    Returns:
        str: The detected language code of the text (e.g., 'ja').
    """

    lang_code, _ = langid.classify(text)

    return lang_code



@tool
def save_script_to_tests_folder(script: str, filename: str) -> str:
    """
    Saves a given script string to the tests/ folder with the specified filename.

    Args:
        script (str): The content of the Python script to save.
        filename (str): Name of the output file (e.g., '001_homepage.py').

    Returns:
        str: Path to the saved script.
    """
    tests_dir = os.path.join(os.path.dirname(__file__), '..', 'tests')
    os.makedirs(tests_dir, exist_ok=True)
    full_path = os.path.join(tests_dir, filename)

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(script)
    print(f"✅ Saved: {filename}")


@tool
def save_screenshot_to_tests_folder(filename: str) -> str:
    """
    Always saves to <project_root>/tests/screenshots/ regardless of current working directory.
    Args:
        filename (str): Name of the screenshot to be saved (e.g., '002.png').
    """
    # Assume this file lives in: <project_root>/agents/tool.py
    tool_file = Path(__file__).resolve()
    project_root = tool_file.parent.parent  # Go up from agents/ to project root

    screenshots_dir = project_root / 'tests' / 'screenshots'
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    screenshot_path = screenshots_dir / filename
    print(f"📸 Screenshot saved: {screenshot_path.resolve()}")
    return str(screenshot_path)