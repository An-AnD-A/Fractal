from src.state.state import State
from src.LLM.HFModel import HFModel


class BasicChatbot:
    
    def __init__(self,
                 llm: HFModel):
        self.llm = llm

    def initiate(self, state: State):
        response = self.llm.define_model().invoke(state['messages'])
        return {'messages': [response]}
