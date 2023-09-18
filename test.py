import os
import openai

openai.api_key = "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"

 
def call_chatgpt_with_memory(messages, model="gpt-3.5-turbo"):
   response = openai.ChatCompletion.create(
       model=model,
       messages=messages,
   )
   return response.choices[0].message["content"]
messages =  [ 
{'role':'system', 'content':'You are friendly chatbot, who will be functioning as the CTO of our new Application'},
  ]

response = call_chatgpt_with_memory(messages)
print(response)
# Output: Yes, your name is Andrea.
def chatgpt_conversation(prompt):
   messages.append({'role':'user', 'content':f"{prompt}"})
   
   response = call_chatgpt_with_memory(messages)
   messages.append({'role':'assistant',
   'content':f"{response}"})
   print(messages)
   return response
chatgpt_conversation("Hello, I am CTO of our company, Let me introduce to our new application Documatic, It is created to revolutionize the Agile and SDLC lifecycle, In this application you need to provide the business idea and it will create the necessary product roadmap, business document, create user stories helps you out the the tech stack, vision document, started code based on DDL command and other important ER diagram")

print("\n\n\n\n\n")
# Output: 'Nice to meet you, Andrea! How can I assist you today?'
chatgpt_conversation("Do you like our business idea ?")

# Output: 'Yes, your name is Andrea.'
print("\n\n\n\n\n")
chatgpt_conversation("Can you suggest some app name for our product")


print("\n\n\n\n\n")
chatgpt_conversation("How about Documatic ?")


print("\n\n\n\n\n")
chatgpt_conversation("Do you understand what our application will do")


print("\n\n\n\n\n")
chatgpt_conversation("Create a vision document")



print("\n\n\n\n\n")
chatgpt_conversation("Create a product roadmap")

print("\n\n\n\n\n")
chatgpt_conversation("Create a ER diagram for our application")

print("\n\n\n\n\n")
chatgpt_conversation("visualize/ draw ER diagram for our application")

print("\n\n\n\n\n")
chatgpt_conversation("generate 10 user stories based on the product roadmap you have created for this quarter")

print("\n\n\n\n\n")
chatgpt_conversation("Create project sequece for 10 of your created user stories")

print("\n\n\n\n\n")
chatgpt_conversation("Create a DDL command based on the ER Diagram provided")

print("\n\n\n\n\n")
chatgpt_conversation("How can we make this application better")

