from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

from typing_extensions import TypedDict


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Devstral-Small-2507",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

def chatbot(state: State):
    return {'messages': [llm.invoke(state['messages'])]}

graph_builder.add_node('Chatbot', chatbot)
graph_builder.add_edge(START, 'Chatbot')
graph_builder.add_edge('Chatbot', END)

# Compile the graph
runnable = graph_builder.compile()

# Run the graph
result = runnable.invoke({'messages': [{'role': 'user', 'content': 'Hello, how are you?'}]})
print(result['messages'])

