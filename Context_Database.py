import pinecone                                                                      # Pinecone is a vector database to store the context
import openai                                                                        # Open AI to use Chat-GPT and LangChain Query

OPENAP_API_KEY = "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"               # API required for to connect Open_API

PINECONE_API_KEY = "85b9b3f1-cadd-4763-a875-368f060e3891"                            # Pinecone API Key
PINECONE_ENVIRONMENT = "gcp-starter"                                                 # Pinecone Environment




def context_db_read_query( index, data, number_of_result, value_required = False ): # Read the parameters based on the openAI chat request and provide the Top 3 results. 

    # return data will have the vector data and top N results, Optionally: include_values (Type: Boolean) will provide the vector as well which is not required in our case
    return_data = index.query( vector = data,           # data = imput provided by the user for current Query
                               top_k = 3,               # value returned based on top_n value 
                               include_values = True )
    
    print( "index query",index.query( vector=data, top_k=3, include_values=True ))
    return return_data




def context_db_write_query(index_name, embed_model, index_Obj):
    user_input = [  "This will considered as second batch of the input",
                    "document of previous user will be provided if top_k is within 3 units "  ]
    
    data = []
    length = len(embedding['data'][0]['embedding'])
    data = embedding['data'][0]['embedding']
    
    embedding = openai.Embedding.create(input= user_input,
                                        engine=embed_model
)
    if index_name not in pinecone.list_indexes():
        print("Creating pinecone index:" + index_name)
        pinecone.create_index(
        index_name,
        dimension=length,
        metric='cosine'
    )
    
    index_Obj.upsert([ 
                       ("user_question_one",
                        embedding['data'][0]['embedding']
                       ) 
                    ])

    print("Description for Index",index_Obj.describe_index_stats())




def context_model_input():
    index_name = "project-guid-2"
    embed_model = "text-embedding-ada-002"
    openai.api_key = "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"
    indexObj = pinecone.Index("project-guid-2")
    api_key = PINECONE_API_KEY
    env = PINECONE_ENVIRONMENT
    pinecone.init(api_key=PINECONE_API_KEY,environment=PINECONE_ENVIRONMENT)
    
    context_db_write_query(index_name, embed_model, indexObj)

