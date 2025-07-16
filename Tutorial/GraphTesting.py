import io
from PIL import Image

from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    number1 : int
    number2 : int
    number3 : int
    number4 : int
    operator1 : str
    operator2 : str
    result1 : int
    result2 : int

def add_node_1(state: State) -> State:
    state['result1'] = state['number1'] + state['number2']
    return state

def add_node_2(state: State) -> State:
    state['result2'] = state['number3'] + state['number4']
    return state

def subtract_node_1(state: State) -> State:
    state['result1'] = state['number1'] - state['number2']
    return state

def subtract_node_2(state: State) -> State:
    state['result2'] = state['number3'] - state['number4']
    return state

def decide_node_1(state: State) -> str:
    if state['operator1'] == '+':
        return 'addition_node_1'
    elif state['operator1'] == '-':
        return 'subtraction_node_1'
    else:
        raise ValueError("Invalid operator for first operation")
    
def decide_node_2(state: State) -> str:
    if state['operator2'] == '+':
        return 'addition_node_2'
    elif state['operator2'] == '-':
        return 'subtraction_node_2'
    else:
        raise ValueError("Invalid operator for second operation")

graph = StateGraph(State)

graph.add_node('router1', lambda state: state)
graph.add_node('router2', lambda state: state)
graph.add_node('add_node_1', add_node_1)
graph.add_node('add_node_2', add_node_2)
graph.add_node('subtract_node_1', subtract_node_1)
graph.add_node('subtract_node_2', subtract_node_2)

graph.add_edge(START, 'router1')
graph.add_conditional_edges(source='router1',
                            path=decide_node_1,
                            path_map={
                                'addition_node_1': 'add_node_1',
                                'subtraction_node_1': 'subtract_node_1'
                            })
graph.add_edge('add_node_1', 'router2')
graph.add_edge('subtract_node_1', 'router2')
graph.add_conditional_edges(source='router2',
                            path=decide_node_2,
                            path_map={
                                'addition_node_2': 'add_node_2',
                                'subtraction_node_2': 'subtract_node_2'
                            })
graph.add_edge('add_node_2', END)
graph.add_edge('subtract_node_2', END)

workflow = graph.compile()
# Visualize the graph
image_bytes = workflow.get_graph().draw_mermaid_png()
img = Image.open(io.BytesIO(image_bytes))
img.show()

# Invoke the graph with an example state
initial_state = {
    'number1': 10,
    'number2': 5,
    'number3': 20,
    'number4': 15,
    'operator1': '+',
    'operator2': '-',
}

result = workflow.invoke(initial_state)
print(result)