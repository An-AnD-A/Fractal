from typing import TypedDict

from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    name: str
    values: list
    response: str

def intro_node(state: State) -> State:
    state['name'] = 'Hello, ' + state['name']
    return state

def processing_node(state:State) -> State:
    state['response'] = state['name'] + '\n' + f'The processed sum of values is : {sum(state["values"])}'
    return state

graph = StateGraph(State)

graph.add_node('IntroNode', intro_node)
graph.add_node('ProcessingNode', processing_node)

graph.add_edge(START, 'IntroNode')
graph.add_edge('IntroNode', 'ProcessingNode')
graph.add_edge('ProcessingNode', END)

workflow = graph.compile()

# Visualize the graph

response = workflow.invoke({'name': 'Bob',
                            'values': [1, 2, 3, 4, 5],})
print(response['response'])