import pinecone                                                                      # Pinecone is a vector database to store the context
import openai                                                                        # Open AI to use Chat-GPT and LangChain Query
import asyncio
OPENAP_API_KEY = "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"               # API required for to connect Open_API

PINECONE_API_KEY = "88425e16-cb6a-40f5-a1da-c289ed1d9269"                            # Pinecone API Key
PINECONE_ENVIRONMENT = "gcp-starter"                                                 # Pinecone Environment




def context_db_read_query( index, data, number_of_result, value_required = False ): # Read the parameters based on the openAI chat request and provide the Top 3 results. 

    # print("Inside context_db_read_query")                                    # This will provide a list of the vector of the query
    
    
    # return data will have the vector data and top N results, Optionally: include_values (Type: Boolean) will provide the vector as well which is not required in our case
    
    return_data = index.query( vector = data,                                       # data = imput provided by the user for current Query
                               top_k = 3,                                           # value returned based on top_n value 
                               include_values = False )
    
    # print( "index query",index.query( vector=data, top_k=3, include_values=False ))
    return return_data



# # Write the data into the Vector Database

def context_db_write_query(index_name, embed_model, index_Obj,current_message):              # Parameter 1: Will require the Project Name of the Context Database, Parameter 2:Wil Require the model type, Parameter 3: will require the instance of the object 
    
    OPENAP_API_KEY = "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"               # API required for to connect Open_API

    PINECONE_API_KEY = "88425e16-cb6a-40f5-a1da-c289ed1d9269"                            # Pinecone API Key
    PINECONE_ENVIRONMENT = "gcp-starter"                                                 # Pinecone Environment

    embed_model = "text-embedding-ada-002"
    openai.api_key = "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"
    pinecone.init(api_key=PINECONE_API_KEY,environment=PINECONE_ENVIRONMENT)
    indexObj = pinecone.Index("project-guid-2")
    api_key = PINECONE_API_KEY
    env = PINECONE_ENVIRONMENT
    user_input = [current_message]
    
    embedding = openai.Embedding.create( input= user_input,                  # This will be used to return the object from Vector Database
                                         engine=embed_model 
                                       )
    data = embedding['data'][0]['embedding']
    length = len(embedding['data'][0]['embedding'])
    if index_name not in pinecone.list_indexes():
        # print("Creating pinecone index:" + index_name)
        pinecone.create_index(
                                index_name,
                                dimension=length,
                                metric='cosine'
                             )

        indexObj.upsert([ 
                       (current_message,
                        embedding['data'][0]['embedding']
                       ) 
                    ])
        return "Completed"

    assistant_data = context_db_read_query(indexObj,data,4,False)
    
    indexObj.upsert([ 
                       (current_message,
                        embedding['data'][0]['embedding']
                       ) 
                    ])

    # print("Description for Index",indexObj.describe_index_stats())
    return assistant_data

def set_context_db_write_query(i,current_message):              # Parameter 1: Will require the Project Name of the Context Database, Parameter 2:Wil Require the model type, Parameter 3: will require the instance of the object 
    OPENAP_API_KEY = "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"               # API required for to connect Open_API
    index_name = "project-guid-2"
    PINECONE_API_KEY = "88425e16-cb6a-40f5-a1da-c289ed1d9269"                            # Pinecone API Key
    PINECONE_ENVIRONMENT = "gcp-starter"                                                 # Pinecone Environment

    embed_model = "text-embedding-ada-002"
    openai.api_key = "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"
    pinecone.init(api_key=PINECONE_API_KEY,environment=PINECONE_ENVIRONMENT)
    indexObj = pinecone.Index("project-guid-2")
    api_key = PINECONE_API_KEY
    env = PINECONE_ENVIRONMENT

    user_input = [current_message]
    
    embedding = openai.Embedding.create( input= user_input,                  # This will be used to return the object from Vector Database
                                         engine=embed_model 
                                       )
    length = len(embedding['data'][0]['embedding'])                         # This will determine the total number of dimension (Axis) of Vector
    data = embedding['data'][0]['embedding']
    if index_name not in pinecone.list_indexes():
        # print("Creating pinecone index:" + index_name)
        pinecone.create_index(
                                index_name,
                                dimension=length,
                                metric='cosine'
                             )
    
    

    indexObj.upsert([ 
                       (current_message[:500],
                        embedding['data'][0]['embedding']
                       ) 
                    ])
    return "Completed"


def context_model_input(current_message):
    index_name = "project-guid-2"
    embed_model = "text-embedding-ada-002"
    openai.api_key = "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"
    indexObj = pinecone.Index("project-guid-2")
    api_key = PINECONE_API_KEY
    env = PINECONE_ENVIRONMENT
    
    pinecone.init(api_key=PINECONE_API_KEY,environment=PINECONE_ENVIRONMENT)
    return context_db_write_query(index_name, embed_model, indexObj, current_message)

