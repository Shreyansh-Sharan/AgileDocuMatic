
import openai

OPENAP_API_KEY = "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"               # API required for to connect Open_API
openai.api_key = "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" 
messages = [
 {"role": "system", "content" : "You’re a kind helpful assistant"}
]

content = input("User: ")
messages.append({"role": "user", "content": content})

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')