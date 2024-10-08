import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How is the weather today in Brasilia",
        }
    ],
    model="gpt-3.5-turbo",
    temperature=1,
)

print(chat_completion.choices[0].message)