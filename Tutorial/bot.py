from dotenv import load_dotenv
from typing import Annotated, TypedDict, List, Union
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage

from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint

from pydantic import BaseModel, Field

from typing_extensions import TypedDict


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational")

chat_model= ChatHuggingFace(llm=llm)

class State(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


def chatbot_node(state: State) -> State:
    response = chat_model.invoke(state['messages'])
    state['messages'].append(AIMessage(content=response.content))
    print(f'AI : {response.content}')
    return state

graph_builder = StateGraph(State)

graph_builder.add_node('chatbot_node', chatbot_node)
graph_builder.add_edge(START, 'chatbot_node')
graph_builder.add_edge('chatbot_node', END)

# Compile the graph
workflow = graph_builder.compile()

conversation_history = []
# Run the graph
user_input = input("Enter: ")
while user_input.lower() != "exit":
    conversation_history.append(HumanMessage(content=user_input))

    result = workflow.invoke({'messages': conversation_history})
    converasation_history = result['messages']
    user_input = input("Enter: ")


