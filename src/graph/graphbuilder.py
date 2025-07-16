from langgraph.graph import StateGraph, START, END

from src.state.state import State
from src.nodes.chatbot import BasicChatbot


class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_graph(self):

        self.chatbot = BasicChatbot(self.llm)
        self.graph_builder.add_node('chatbot', self.chatbot.initiate())
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_edge('chatbot', END)