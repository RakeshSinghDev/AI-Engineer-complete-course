
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load environment variables
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

# 2. Create Groq client
client = Groq(api_key=my_api_key)

# 3. Select model
model = "openai/gpt-oss-120b"

# 4. User prompt
prompt = "What is Machine Learning?"

# 5. Send request to Groq
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# 6. Extract AI response
answer = response.choices[0].message.content

# 7. Print answer
print(answer)
