

class perceptron:
    """
    What all required at a perceptron layer

    - We would need a weight matrix and bias matrix for the number of inputs.
    - we would need the activation that happen at the perceptron.
    - we would need the functionality to take in the input matrix.
    - we would need the functionality to compute the perceptron level calculations.
    - we would need to initiate the perceptron without the need of a initial weight matrix i,e for the first time the 
        weight matrix needs to be initiated by the object itself.

    """
    def __init__(self):
        self.weights = []
        self.bias = 0.0
        self.activation = 0.0

    def feedforward(self, inputs):
    
        