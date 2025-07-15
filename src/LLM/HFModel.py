from typing import Annotated, Literal

from langchain_huggingface import HuggingFaceEndpoint

"""
Developer Note
--------------

- Need to create a function to pass the model parameter to the Huggingface model.
"""

class HFModel:

    def __init__(self, 
                 model: str):
        """
        The class object will store the Huggingface Model details and initiate the model.
        
        Parameters
        ----------
        model : str
            The Huggingface model to be used.
        """
        
        self.model = model

    def define_model(self):
        """
        Function to define the Huggingface model.
        """
        
        llm = HuggingFaceEndpoint(
            repo_id=self.model,
            provider="auto",
        )

        return llm

if __name__ == "__main__":
    model = HFModel(model="mistralai/Devstral-Small-2507")
    llm = model.define_model()
    print(f"Model {model.model} initialized successfully.")

