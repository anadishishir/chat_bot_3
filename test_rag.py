from src.retrieve import retrieve 
from src.llm import generate_answer 

question = "What is this document about?" 

docs = retrieve(question) 

context = "\n".join(docs) 

answer = generate_answer(
    question,
    context
) 

print(answer) 