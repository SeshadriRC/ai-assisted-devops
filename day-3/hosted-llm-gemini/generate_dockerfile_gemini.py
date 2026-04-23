from google import genai
import os

# Set your API key here
os.environ["GOOGLE_API_KEY"] = "xxxxxxxxxxxxxxxx"

# Configure the Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. Just share the dockerfile without any explanation between two lines to make copying dockerfile easy.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    response = client.models.generate_content(
        model='models/gemma-4-31b-it',
        contents=PROMPT.format(language=language)
    )
    return response.text

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)

