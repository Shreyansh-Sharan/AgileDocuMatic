import openai
from openai.embeddings_utils import get_embedding, cosine_similarity
openai.api_key = "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"
embedding1 = get_embedding("Who is mr. Beast",engine='text-embedding-ada-002')
embedding2 = get_embedding("What does he do ?",engine="text-embedding-ada-002")
print(cosine_similarity(embedding1, embedding2))

print(embedding1)