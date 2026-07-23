import os
from dotenv import load_dotenv
from openai import OpenAI

#loading open router API key
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("openrouter api key is not connected! \nCheck your env")

#making a clien using openai
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

message=[
    {
        "role": "user",
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]

response = client.chat.completions.create(
    model = "openrouter/free",
    messages=message
    )
if response.usage == None:
    raise RuntimeError("Failed API request")

print(f"Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")
print(response.choices[0].message.content)

def main():
    print("Hello from ai-clibot!")


if __name__ == "__main__":
    main()
