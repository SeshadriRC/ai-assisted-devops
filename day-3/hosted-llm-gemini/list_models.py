from google import genai
import os

os.environ["GOOGLE_API_KEY"] = "xxxx"

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available models:")
for model in client.models.list():
    print(f"- {model.name}")
