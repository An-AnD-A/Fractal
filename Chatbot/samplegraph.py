from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict

from typing import Annotated
from langgraph.graph.message import add_messages

from PIL import Image
import io

# Define the schema for the node states
class state(TypedDict):
    text: str

# class llmstate(TypedDict):
#     messages: Annotated[list, add_messages]

# # Define the llm model for the llm node
# llm = init_chat_model(
#     model_name="antropic:claude-3-5-sonnet-latest"
# )

# Define the Node Functions
def node1(state):
    state['text'] += 'Node 1 processing.\n'
    return state

# def llm_model(llmstate):
#     return {'messages': [llm.invoke(llmstate['messages'])]}

def node2(state):
    state['text'] += 'Node 2 processing.\n'
    return state

# Define the state graph
workflow = StateGraph(state)

# Define the Graph Nodes
workflow.add_node('Node 1', node1)
# workflow.add_node('LLM Node', llm_model)
workflow.add_node('Node 2', node2)

# Define the Gra[h Edges]
workflow.add_edge(START, 'Node 1')
# workflow.add_edge('Node 1', 'LLM Node')
workflow.add_edge('Node 1', 'Node 2')
# workflow.add_edge('LLM Node', 'Node 2')
workflow.add_edge('Node 2', END)

# Compile the Graph
runnable = workflow.compile()

# Run the graph
result = runnable.invoke({'text': 'Starting process: \n'})
print(result['text'])

print('Creating graph visualization...')
image_bytes = runnable.get_graph().draw_mermaid_png()
img = Image.open(io.BytesIO(image_bytes))
img.show()