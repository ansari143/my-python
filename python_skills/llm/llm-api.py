import os
from openai import OpenAI

# Ensure OPENAI_API_KEY is set in your environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#print(os.getenv("OPENAI_API_KEY"))
text_input = str(input("Enter your prompt: "))
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": text_input
    }],
    response_format={
        "type": "text"
    },
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
for choice in response.choices:
    print(choice.message.content)
