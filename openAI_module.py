import time
import openai
from openai import util
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource
from openai.error import TryAgain
import Context_Database
import asyncio

# content = input("User: ")
# messages.append({"role":'user', "content":content})

# completion = openai.ChatCompletion.create( model = 'gpt-3.5-turbo',
#                                            message = messages)

# 
openai.api_key = "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" 

def set_system_message():
    return {"role": "system","content":" You are the CTO for a startup  revolutionising the Agile and SDLC lifecycle by using the Open AI tools. Client will provide a business requirement document based on that we will create a vision document, product roadmap, software architecture diagram and user stories."}
           

def get_API_keys():
    OPENAP_API_KEY = "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"               # API required for to connect Open_API
    PINECONE_API_KEY = "85b9b3f1-cadd-4763-a875-368f060e3891"                            # Pinecone API Key
    PINECONE_ENVIRONMENT = "gcp-starter"                                                 

def set_chat_context():
    get_API_keys()
    
    print(""" Welcome to the application: For the next five question, Please provide the Business Overview, App Idea, Provide a basic functionality of the application, Vision Document, Product Roadmap Template """ )
    for i in range(5):
        
        user_context_input = input("Please provide a Business Overview \n")
        if i == 0:
            chat_context_message = [{"role":"system","content":user_context_input}]
            print(chat_context_message)
        else:
            chat_context_message = [{"role":"system","content":user_context_input}]
        completion = openai.ChatCompletion.create(
                                                    model="gpt-3.5-turbo",
                                                    messages = chat_context_message
                                                )

        chat_response = completion.choices[0]["message"]["content"]
        final_response = f"Question: {user_context_input} - AgileDocumatic Response: {chat_response}"
        print(final_response)
        print("oustide the storing procedure",Context_Database.set_context_db_write_query(i,final_response))
        print(f"Your Data {i} is stored successfully in the Vector Database")
    

def poc_chatbot():
    system_message = set_system_message()
    get_API_keys() 

    print("""Initiating Agile - DocuMatic: One stop solution to create a intitiation document for all your agile process and create a basic code.
             Enter you prompt to start the product idea or type quit to Quit the backend """)
    
    last_message = ""


    while True:
        context_message = []
        # context_message.append(system_message)
        current_message = input("User: Ask your question")
        copy_current = current_message[:]
        current_message += last_message
        # print(current_message)
        if current_message.lower() == "quit":
            break
        assistant_messages = Context_Database.context_model_input(current_message)
        # print(assistant_messages)
        
        for i in range(2):
            print(f"{assistant_messages['matches'][0]['id']}")
            print(f"{assistant_messages['matches'][1]['id']}")
            print(f"{assistant_messages['matches'][2]['id']}")
            j = input("Select the best command that you wanted to include")
            current_message += f"{assistant_messages['matches'][int(j)]['id']}"
        # context_message.append({'role':'assistant',"content":assistant_messages['matches'][int(j)]['id']})
        context_message.append({'role':'user',"content":current_message})

        print("\n\n\n\n\n\n\n Asking question about",context_message,"/n/n/n/n/n")
        completion = openai.ChatCompletion.create(
                                                    model="gpt-3.5-turbo-16k",
                                                    messages=context_message
                                                )

        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
        context_message.clear()
        last_message = copy_current+chat_response
        
        
if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit' to stop)!")
    set_chat_context()
    poc_chatbot()
    
