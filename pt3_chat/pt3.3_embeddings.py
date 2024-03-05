# Embeddings refer to a mathematical representation of data, often used in machine learning and natural language processing tasks. In the context of natural language processing (NLP), word embeddings are particularly common. These are numerical representations of words, typically in the form of dense vectors, where each dimension of the vector captures certain semantic or syntactic properties of the word.

"""
from openai import OpenAI
client = OpenAI(api_key='')

response = client.embeddings.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter...",
  encoding_format="float"
)

print(response)
"""

# The embedding object

"""
{
  "object": "embedding",
  "embedding": [
    0.0023064255,
    -0.009327292,
    .... (1536 floats total for ada-002)
    -0.0028842222,
  ],
  "index": 0
}
"""