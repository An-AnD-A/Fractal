import numpy as np

from typing import List, Optional

from Activations.linear import linear_activation
from Activations.ReLU import ReLU_activation
from Activations.Sigmoid import Sigmoid_activation

class perceptron:
    """
    Class object that defines a single perceptron and the calculations that happen within.

    Developer Notes
    ---------------
    What all required at a perceptron layer

    - We would need a weight matrix and bias matrix for the number of inputs.
    - we would need the activation that happen at the perceptron.
    - we would need the functionality to take in the input matrix.
    - we would need the functionality to compute the perceptron level calculations.
    - we would need to initiate the perceptron without the need of a initial weight matrix i,e for the first time the 
        weight matrix needs to be initiated by the object itself.

    """
    def __init__(self,
                 weights: Optional[np.ndarray] = None,
                 bias: float = 0.0,
                 inputs: Optional[np.ndarray] = None,
                 activation: str = "linear",
                 output: Optional[float] = None):
        """
        Initialize the perceptron.

        Parameters
        ----------
        weights : Optional[np.ndarray]
            Weight vector; if None, must be set before feedforward.
        bias : float
            Bias term (default 0.0).
        activation : str
            Activation function name (default "linear").
        inputs : Optional[np.ndarray]
            Input vector; if None, must be set before feedforward
        output : Optional[float]
            Activated output; if None, will be computed.
        """
        self.weights = weights
        self.bias = bias
        self.inputs = inputs
        self.activation = activation
        self.output = self._perceptron_calculate()

    def _perceptron_calculate(self) -> float:
        """
        Perform the perceptron calculation: compute pre-activation and apply activation function.

        Returns
        -------
        float
            The activated output.
        """
        preactivation = self._preactivation_compute()
        activated_output = self._activation_compute(preactivation)

        self.output = activated_output

        return self.output

    def _preactivation_compute(self) -> float:
        """
        Compute the pre-activation value (weighted sum plus bias).

        Returns
        -------
        float
            The pre-activation value.
        """
        if self.weights is None or self.inputs is None:
            raise ValueError("Weights and inputs must be set before computing pre-activation.")
        return np.dot(self.inputs, self.weights) + self.bias
    
    def _activation_compute(self, preactivation: float) -> float:
        """
        Apply the activation function to the pre-activation value.

        Parameters
        ----------
        preactivation : float
            The pre-activation value.

        Returns
        -------
        float
            The activated output.
        """
        if self.activation == "linear":
            result = linear_activation(preactivation)
            return result
        
        elif self.activation == "relu":
            result = ReLU_activation(preactivation)
            return result
        
        elif self.activation == "sigmoid":
            result = Sigmoid_activation(preactivation)
            return result
        else:
            raise ValueError(f"Unsupported activation function: {self.activation}")
        
if __name__ == "__main__":
    # Example usage
    p = perceptron(weights=np.array([0.2, -0.6]), 
                   bias=0.1, 
                   inputs=np.array([1.0, 2.0]), 
                   activation="linear")
    
    preactivation = p._preactivation_compute()
    activated_output = p._activation_compute(preactivation)

    print(f"Pre-activation: {preactivation}, Activated output: {activated_output}")